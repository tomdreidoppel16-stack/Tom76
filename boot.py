"""Extract bundled TomGPT source on first deployment. All GitHub files can stay flat."""
from __future__ import annotations
import argparse
import base64
import hashlib
from io import BytesIO
from pathlib import Path
import zipfile


def extract(dest: str|Path='.', dry_run: bool=False) -> dict:
    from core_bundle import DATA_B85, SHA256, FILE_COUNT
    packed=base64.b85decode(DATA_B85)
    if hashlib.sha256(packed).hexdigest() != SHA256:
        raise RuntimeError('Bundled source checksum mismatch, stopping.')
    target=Path(dest).resolve()
    count=0
    with zipfile.ZipFile(BytesIO(packed),'r') as z:
        for file in z.infolist():
            if file.is_dir():
                continue
            path=Path(file.filename)
            # Defend against accidental path traversal even with embedded package.
            if path.is_absolute() or '..' in path.parts or path.parts[0] not in ('tomgpt','demos','tests'):
                raise RuntimeError(f'Unexpected bundled path: {path}')
            if file.file_size>2*1024*1024:
                raise RuntimeError(f'Unexpected oversized file: {path}')
            output=(target/path).resolve()
            if not output.is_relative_to(target):
                raise RuntimeError('Unsafe extraction destination')
            if not dry_run:
                output.parent.mkdir(parents=True,exist_ok=True)
                output.write_bytes(z.read(file.filename))
            count+=1
    if count != FILE_COUNT:
        raise RuntimeError(f'Expected {FILE_COUNT} files, found {count}')
    return {'verified':True, 'files':count, 'output':str(target), 'extracted':not dry_run}


def main():
    ap=argparse.ArgumentParser(description='TomGPT one-folder deploy bootstrap')
    ap.add_argument('--extract',action='store_true',help='Extract project source into tomgpt/ and demos/')
    ap.add_argument('--verify',action='store_true',help='Verify embedded archive and paths without extracting')
    ap.add_argument('--dest',default='.',help='Destination folder (default: current directory)')
    args=ap.parse_args()
    if not args.extract and not args.verify:
        ap.error('Choose --extract or --verify')
    print(extract(args.dest,dry_run=not args.extract))

if __name__=='__main__':
    main()
