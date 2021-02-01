# Zipstrings

Zipstrings is a strings helper utility with archive file format support 📦.

Zipstrings can be very useful helper utility when analyzing extracted firmware images. It utilizes the `strings` util and adds support for several archive file formats, like `zip`, `jar`, `xlsx`, `docx`, `apk` or `apex`. This will enhance the ability to find relevant parts of a firmware during an analysis. Zipstrings can be pretty useful in a completely different context as well.

More information on why zipstrings was initially developed can be found [here](https://www.jakoblell.com/blog/2013/08/25/advanced-grepping-through-directory-trees-with-binary-data/).

## Trying it out

To find the printable strings of objects (including archives), or other binary or files in a directory, issue the following command:

```python
$ ./zipstrings.py <dir>
```

Note: It is recommended to save the zipstrings output in a file (e.g. to allow faster searches in the output):

```python
$ ./zipstrings.py <dir> > <output filename>
```