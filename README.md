# Zipstrings

Zipstrings is a strings helper utility with archive file format support 📦.

Zipstrings can be very useful helper utility when analyzing extracted firmware images. It utilizes the `strings` util and adds support for several archive file formats, like `zip`, `jar`, `xlsx`, `docx`, `apk` or `apex`. This will enhance the ability to find relevant parts of a firmware during an analysis. Zipstrings can be pretty useful in a completely different context as well.

## Trying it out

To find the printable strings of objects (including archives), or other binary or files in a directory, issue the following command:

```python
$ python3 zipstrings.py <dir>
```

