# regex-spellcheck
Simple spellchecker that finds mistakes with regular expressions.

## Dependencies

 * termcolor

## Usage

```bash
./spellcheck.py FILE [FILE ...]
```

Options are:
 * `--help` to show this help message and exit
 * `--whitespace` to also detect whitespace issues
 * `--all` to print all matches at once without interaction

## Credits

 * http://tech.aabouzaid.com/2015/12/libreoffice-macro-to-fix-common-mistakes-with-regex-python.html
 * http://andrewknighton.com/using-regular-expressions-to-find-common-errors-a-guest-post-by-russell-phillips/

## TODOs

 * Add more useful regular expressions
 * Write corrections into new file
 * Support to enter custom corrections
