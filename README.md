## Installation:
Requirements: Python 3, node, bash, qpdf, OSX GNU coreutils

### System dependencies:
Only OSX is supported at the moment.

* qpdf: `brew install qpdf`
* gtimeout: `brew install coreutils`

But that is because these are terrible bash scripts. We should fix that!

### Python:
```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Node:
`npm install`

## Usage:
1. `./download.sh` <-- This downloads the front page of today's newspapers into `data/[date]/`
2. `./decrypt.sh` <-- This runs all the pdfs through a passwordless decrypt (automatically done by pdf viewers), and deletes the original pdfs.
3. `./parse.sh` <-- This extracts xml files from the decrypted pdfs, and saves them in the same data directory.
