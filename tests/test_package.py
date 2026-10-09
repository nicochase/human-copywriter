import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

module_path = Path(__file__).resolve().parents[1] / 'scripts' / 'manage.py'
spec = importlib.util.spec_from_file_location('manage', module_path)
manage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(manage)


class PackageTests(unittest.TestCase):
    def test_archive_roundtrip_and_reproducibility(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            archive = manage.package(folder)
            first = archive.read_bytes()
            with zipfile.ZipFile(archive) as bundle:
                expected = {f'{manage.NAME}/{path}': data for path, data in manage.check().items()}
                self.assertEqual(set(bundle.namelist()), set(expected))
                self.assertEqual({path: bundle.read(path) for path in bundle.namelist()}, expected)
                bundle.extractall(folder / 'extracted')
            self.assertEqual(manage.check(folder / 'extracted' / manage.NAME), manage.check())
            manage.package(folder)
            self.assertEqual(archive.read_bytes(), first)

    def test_install_idempotence_and_conflict_preservation(self):
        with tempfile.TemporaryDirectory() as directory:
            target, status = manage.install(directory)
            self.assertEqual(manage.inventory(target), manage.check())
            self.assertIn('installed', status)
            self.assertEqual(manage.install(directory)[1], 'already identical')
            custom = target / 'personal-note.md'
            custom.write_text('preserve me')
            with self.assertRaises(ValueError):
                manage.install(directory)
            self.assertEqual(custom.read_text(), 'preserve me')

    def test_symlinks_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            (folder / manage.NAME).symlink_to(manage.SKILL, target_is_directory=True)
            with self.assertRaises(ValueError):
                manage.install(folder)

    def test_missing_relative_reference_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            installed, _ = manage.install(directory)
            (installed / 'references' / 'humanizer.md').unlink()
            with self.assertRaises(ValueError):
                manage.check(installed)


if __name__ == '__main__':
    unittest.main()
