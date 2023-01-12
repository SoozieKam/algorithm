# Python: 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)]
# Library: io, version: unspecified
# Module: io, version: unspecified

"The io module provides the Python interfaces to stream handling. The\nbuiltin open function is defined in this module.\n\nAt the top of the I/O hierarchy is the abstract base class IOBase. It\ndefines the basic interface to a stream. Note, however, that there is no\nseparation between reading and writing to streams; implementations are\nallowed to raise an OSError if they do not support a given operation.\n\nExtending IOBase is RawIOBase which deals simply with the reading and\nwriting of raw bytes to a stream. FileIO subclasses RawIOBase to provide\nan interface to OS files.\n\nBufferedIOBase deals with buffering on a raw byte stream (RawIOBase). Its\nsubclasses, BufferedWriter, BufferedReader, and BufferedRWPair buffer\nstreams that are readable, writable, and both respectively.\nBufferedRandom provides a buffered interface to random access\nstreams. BytesIO is a simple stream of in-memory bytes.\n\nAnother IOBase subclass, TextIOBase, deals with the encoding and decoding\nof streams into text. TextIOWrapper, which extends it, is a buffered text\ninterface to a buffered raw stream (`BufferedIOBase`). Finally, StringIO\nis an in-memory stream for text.\n\nArgument names are not part of the specification, and only the arguments\nof open() are intended to be used as keyword arguments.\n\ndata:\n\nDEFAULT_BUFFER_SIZE\n\n   An int containing the default buffer size used by the module's buffered\n   I/O classes. open() uses the file's blksize (as obtained by os.stat) if\n   possible.\n"

import typing
import builtins as _mod_builtins
import io as _mod_io

BlockingIOError = _mod_builtins.BlockingIOError
class BufferedRWPair(_BufferedIOBase):
    'A buffered reader and writer object together.\n\nA buffered reader object and buffered writer object put together to\nform a sequential IO object that can read and write. This is typically\nused with a socket or two-way pipe.\n\nreader and writer are RawIOBase objects that are readable and\nwriteable respectively. If the buffer_size is omitted it defaults to\nDEFAULT_BUFFER_SIZE.'
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'A buffered reader and writer object together.\n\nA buffered reader object and buffered writer object put together to\nform a sequential IO object that can read and write. This is typically\nused with a socket or two-way pipe.\n\nreader and writer are RawIOBase objects that are readable and\nwriteable respectively. If the buffer_size is omitted it defaults to\nDEFAULT_BUFFER_SIZE.'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def close(self) -> typing.Any:
        ...
    
    @property
    def closed(self) -> typing.Any:
        ...
    
    def flush(self) -> typing.Any:
        ...
    
    def isatty(self) -> typing.Any:
        ...
    
    def peek(self) -> typing.Any:
        ...
    
    def read(self) -> typing.Any:
        ...
    
    def read1(self) -> typing.Any:
        ...
    
    def readable(self) -> typing.Any:
        ...
    
    def readinto(self) -> typing.Any:
        ...
    
    def readinto1(self) -> typing.Any:
        ...
    
    def writable(self) -> typing.Any:
        ...
    
    def write(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class BufferedRandom(_BufferedIOBase):
    'A buffered interface to random access streams.\n\nThe constructor creates a reader and writer for a seekable stream,\nraw, given in the first argument. If the buffer_size is omitted it\ndefaults to DEFAULT_BUFFER_SIZE.'
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'A buffered interface to random access streams.\n\nThe constructor creates a reader and writer for a seekable stream,\nraw, given in the first argument. If the buffer_size is omitted it\ndefaults to DEFAULT_BUFFER_SIZE.'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __next__(self) -> typing.Any:
        'Implement next(self).'
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    def __sizeof__(self) -> int:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _dealloc_warn(self) -> typing.Any:
        ...
    
    @property
    def _finalizing(self) -> typing.Any:
        ...
    
    def close(self) -> typing.Any:
        ...
    
    @property
    def closed(self) -> typing.Any:
        ...
    
    def detach(self) -> typing.Any:
        ...
    
    def fileno(self) -> typing.Any:
        ...
    
    def flush(self) -> typing.Any:
        ...
    
    def isatty(self) -> typing.Any:
        ...
    
    @property
    def mode(self) -> typing.Any:
        ...
    
    @property
    def name(self) -> typing.Any:
        ...
    
    def peek(self, size) -> typing.Any:
        ...
    
    @property
    def raw(self) -> typing.Any:
        ...
    
    def read(self, size) -> typing.Any:
        ...
    
    def read1(self, size) -> typing.Any:
        ...
    
    def readable(self) -> typing.Any:
        ...
    
    def readinto(self, buffer) -> typing.Any:
        ...
    
    def readinto1(self, buffer) -> typing.Any:
        ...
    
    def readline(self, size) -> typing.Any:
        ...
    
    def seek(self, target, whence) -> typing.Any:
        ...
    
    def seekable(self) -> typing.Any:
        ...
    
    def tell(self) -> typing.Any:
        ...
    
    def truncate(self, pos) -> typing.Any:
        ...
    
    def writable(self) -> typing.Any:
        ...
    
    def write(self, buffer) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class BufferedReader(_BufferedIOBase):
    'Create a new buffered reader using the given readable raw IO object.'
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Create a new buffered reader using the given readable raw IO object.'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __next__(self) -> typing.Any:
        'Implement next(self).'
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    def __sizeof__(self) -> int:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _dealloc_warn(self) -> typing.Any:
        ...
    
    @property
    def _finalizing(self) -> typing.Any:
        ...
    
    def close(self) -> typing.Any:
        ...
    
    @property
    def closed(self) -> typing.Any:
        ...
    
    def detach(self) -> typing.Any:
        ...
    
    def fileno(self) -> typing.Any:
        ...
    
    def flush(self) -> typing.Any:
        ...
    
    def isatty(self) -> typing.Any:
        ...
    
    @property
    def mode(self) -> typing.Any:
        ...
    
    @property
    def name(self) -> typing.Any:
        ...
    
    def peek(self, size) -> typing.Any:
        ...
    
    @property
    def raw(self) -> typing.Any:
        ...
    
    def read(self, size) -> typing.Any:
        ...
    
    def read1(self, size) -> typing.Any:
        ...
    
    def readable(self) -> typing.Any:
        ...
    
    def readinto(self, buffer) -> typing.Any:
        ...
    
    def readinto1(self, buffer) -> typing.Any:
        ...
    
    def readline(self, size) -> typing.Any:
        ...
    
    def seek(self, target, whence) -> typing.Any:
        ...
    
    def seekable(self) -> typing.Any:
        ...
    
    def tell(self) -> typing.Any:
        ...
    
    def truncate(self, pos) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class BufferedWriter(_BufferedIOBase):
    'A buffer for a writeable sequential RawIO object.\n\nThe constructor creates a BufferedWriter for the given writeable raw\nstream. If the buffer_size is not given, it defaults to\nDEFAULT_BUFFER_SIZE.'
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'A buffer for a writeable sequential RawIO object.\n\nThe constructor creates a BufferedWriter for the given writeable raw\nstream. If the buffer_size is not given, it defaults to\nDEFAULT_BUFFER_SIZE.'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    def __sizeof__(self) -> int:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _dealloc_warn(self) -> typing.Any:
        ...
    
    @property
    def _finalizing(self) -> typing.Any:
        ...
    
    def close(self) -> typing.Any:
        ...
    
    @property
    def closed(self) -> typing.Any:
        ...
    
    def detach(self) -> typing.Any:
        ...
    
    def fileno(self) -> typing.Any:
        ...
    
    def flush(self) -> typing.Any:
        ...
    
    def isatty(self) -> typing.Any:
        ...
    
    @property
    def mode(self) -> typing.Any:
        ...
    
    @property
    def name(self) -> typing.Any:
        ...
    
    @property
    def raw(self) -> typing.Any:
        ...
    
    def seek(self, target, whence) -> typing.Any:
        ...
    
    def seekable(self) -> typing.Any:
        ...
    
    def tell(self) -> typing.Any:
        ...
    
    def truncate(self, pos) -> typing.Any:
        ...
    
    def writable(self) -> typing.Any:
        ...
    
    def write(self, buffer) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class BytesIO(_BufferedIOBase):
    'Buffered I/O implementation using an in-memory bytes buffer.'
    __dict__: typing.Dict[str, typing.Any]
    def __getstate__(self) -> typing.Any:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        'Buffered I/O implementation using an in-memory bytes buffer.'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __iter__(self) -> BytesIO:
        'Implement iter(self).'
        ...
    
    def __next__(self) -> typing.Any:
        'Implement next(self).'
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    def __sizeof__(self) -> int:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def close(self) -> typing.Any:
        'Disable all I/O operations.'
        ...
    
    @property
    def closed(self) -> typing.Any:
        'True if the file is closed.'
        ...
    
    def flush(self) -> typing.Any:
        'Does nothing.'
        ...
    
    def getbuffer(self) -> typing.Any:
        'Get a read-write view over the contents of the BytesIO object.'
        ...
    
    def getvalue(self) -> typing.Any:
        'Retrieve the entire contents of the BytesIO object.'
        ...
    
    def isatty(self) -> typing.Any:
        'Always returns False.\n\nBytesIO objects are not connected to a TTY-like device.'
        ...
    
    def read(self, size) -> typing.Any:
        'Read at most size bytes, returned as a bytes object.\n\nIf the size argument is negative, read until EOF is reached.\nReturn an empty bytes object at EOF.'
        ...
    
    def read1(self, size) -> typing.Any:
        'Read at most size bytes, returned as a bytes object.\n\nIf the size argument is negative or omitted, read until EOF is reached.\nReturn an empty bytes object at EOF.'
        ...
    
    def readable(self) -> typing.Any:
        'Returns True if the IO object can be read.'
        ...
    
    def readinto(self, buffer) -> typing.Any:
        'Read bytes into buffer.\n\nReturns number of bytes read (0 for EOF), or None if the object\nis set not to block and has no data to read.'
        ...
    
    def readline(self, size) -> typing.Any:
        'Next line from the file, as a bytes object.\n\nRetain newline.  A non-negative size argument limits the maximum\nnumber of bytes to return (an incomplete line may be returned then).\nReturn an empty bytes object at EOF.'
        ...
    
    def readlines(self, size) -> typing.Any:
        'List of bytes objects, each a line from the file.\n\nCall readline() repeatedly and return a list of the lines so read.\nThe optional size argument, if given, is an approximate bound on the\ntotal number of bytes in the lines returned.'
        ...
    
    def seek(self, pos, whence) -> typing.Any:
        'Change stream position.\n\nSeek to byte offset pos relative to position indicated by whence:\n     0  Start of stream (the default).  pos should be >= 0;\n     1  Current position - pos may be negative;\n     2  End of stream - pos usually negative.\nReturns the new absolute position.'
        ...
    
    def seekable(self) -> typing.Any:
        'Returns True if the IO object can be seeked.'
        ...
    
    def tell(self) -> typing.Any:
        'Current file position, an integer.'
        ...
    
    def truncate(self, size) -> typing.Any:
        'Truncate the file to at most size bytes.\n\nSize defaults to the current file position, as returned by tell().\nThe current file position is unchanged.  Returns the new size.'
        ...
    
    def writable(self) -> typing.Any:
        'Returns True if the IO object can be written.'
        ...
    
    def write(self, b) -> typing.Any:
        'Write bytes to file.\n\nReturn the number of bytes written.'
        ...
    
    def writelines(self, lines) -> typing.Any:
        'Write lines to the file.\n\nNote that newlines are not added.  lines can be any iterable object\nproducing bytes-like objects. This is equivalent to calling write() for\neach element.'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

DEFAULT_BUFFER_SIZE: int
class FileIO(_RawIOBase):
    "Open a file.\n\nThe mode can be 'r' (default), 'w', 'x' or 'a' for reading,\nwriting, exclusive creation or appending.  The file will be created if it\ndoesn't exist when opened for writing or appending; it will be truncated\nwhen opened for writing.  A FileExistsError will be raised if it already\nexists when opened for creating. Opening a file for creating implies\nwriting so this mode behaves in a similar way to 'w'.Add a '+' to the mode\nto allow simultaneous reading and writing. A custom opener can be used by\npassing a callable as *opener*. The underlying file descriptor for the file\nobject is then obtained by calling opener with (*name*, *flags*).\n*opener* must return an open file descriptor (passing os.open as *opener*\nresults in functionality similar to passing None)."
    __dict__: typing.Dict[str, typing.Any]
    def __getattribute__(self, name) -> typing.Any:
        'Return getattr(self, name).'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        "Open a file.\n\nThe mode can be 'r' (default), 'w', 'x' or 'a' for reading,\nwriting, exclusive creation or appending.  The file will be created if it\ndoesn't exist when opened for writing or appending; it will be truncated\nwhen opened for writing.  A FileExistsError will be raised if it already\nexists when opened for creating. Opening a file for creating implies\nwriting so this mode behaves in a similar way to 'w'.Add a '+' to the mode\nto allow simultaneous reading and writing. A custom opener can be used by\npassing a callable as *opener*. The underlying file descriptor for the file\nobject is then obtained by calling opener with (*name*, *flags*).\n*opener* must return an open file descriptor (passing os.open as *opener*\nresults in functionality similar to passing None)."
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def _blksize(self) -> typing.Any:
        ...
    
    def _dealloc_warn(self) -> typing.Any:
        ...
    
    @property
    def _finalizing(self) -> typing.Any:
        ...
    
    def close(self) -> typing.Any:
        'Close the file.\n\nA closed file cannot be used for further I/O operations.  close() may be\ncalled more than once without error.'
        ...
    
    @property
    def closed(self) -> typing.Any:
        'True if the file is closed'
        ...
    
    @property
    def closefd(self) -> typing.Any:
        'True if the file descriptor will be closed by close().'
        ...
    
    def fileno(self) -> typing.Any:
        'Return the underlying file descriptor (an integer).'
        ...
    
    def isatty(self) -> typing.Any:
        'True if the file is connected to a TTY device.'
        ...
    
    @property
    def mode(self) -> typing.Any:
        'String giving the file mode'
        ...
    
    def read(self, size) -> typing.Any:
        'Read at most size bytes, returned as bytes.\n\nOnly makes one system call, so less data may be returned than requested.\nIn non-blocking mode, returns None if no data is available.\nReturn an empty bytes object at EOF.'
        ...
    
    def readable(self) -> typing.Any:
        'True if file was opened in a read mode.'
        ...
    
    def readall(self) -> typing.Any:
        'Read all data from the file, returned as bytes.\n\nIn non-blocking mode, returns as much as is immediately available,\nor None if no data is available.  Return an empty bytes object at EOF.'
        ...
    
    def readinto(self, buffer) -> typing.Any:
        'Same as RawIOBase.readinto().'
        ...
    
    def seek(self, pos, whence) -> typing.Any:
        'Move to new file position and return the file position.\n\nArgument offset is a byte count.  Optional argument whence defaults to\nSEEK_SET or 0 (offset from start of file, offset should be >= 0); other values\nare SEEK_CUR or 1 (move relative to current position, positive or negative),\nand SEEK_END or 2 (move relative to end of file, usually negative, although\nmany platforms allow seeking beyond the end of a file).\n\nNote that not all file objects are seekable.'
        ...
    
    def seekable(self) -> typing.Any:
        'True if file supports random-access.'
        ...
    
    def tell(self) -> typing.Any:
        'Current file position.\n\nCan raise OSError for non seekable files.'
        ...
    
    def truncate(self, size) -> typing.Any:
        'Truncate the file to at most size bytes and return the truncated size.\n\nSize defaults to the current file position, as returned by tell().\nThe current file position is changed to the value of size.'
        ...
    
    def writable(self) -> typing.Any:
        'True if file was opened in a write mode.'
        ...
    
    def write(self, b) -> typing.Any:
        'Write buffer b to file, return number of bytes written.\n\nOnly makes one system call, so not all of the data may be written.\nThe number of bytes actually written is returned.  In non-blocking mode,\nreturns None if the write would block.'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class IncrementalNewlineDecoder(_mod_builtins.object):
    'Codec used when reading a file in universal newlines mode.\n\nIt wraps another incremental decoder, translating \\r\\n and \\r into \\n.\nIt also records the types of newlines encountered.  When used with\ntranslate=False, it ensures that the newline sequence is returned in\none piece. When used with decoder=None, it expects unicode strings as\ndecode input and translates newlines without first invoking an external\ndecoder.'
    def __init__(self, *args, **kwargs) -> None:
        'Codec used when reading a file in universal newlines mode.\n\nIt wraps another incremental decoder, translating \\r\\n and \\r into \\n.\nIt also records the types of newlines encountered.  When used with\ntranslate=False, it ensures that the newline sequence is returned in\none piece. When used with decoder=None, it expects unicode strings as\ndecode input and translates newlines without first invoking an external\ndecoder.'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def decode(self, input, final) -> typing.Any:
        ...
    
    def getstate(self) -> typing.Any:
        ...
    
    @property
    def newlines(self) -> typing.Any:
        ...
    
    def reset(self) -> typing.Any:
        ...
    
    def setstate(self, state) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class StringIO(_TextIOBase):
    "Text I/O implementation using an in-memory buffer.\n\nThe initial_value argument sets the value of object.  The newline\nargument is like the one of TextIOWrapper's constructor."
    __dict__: typing.Dict[str, typing.Any]
    def __getstate__(self) -> typing.Any:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        "Text I/O implementation using an in-memory buffer.\n\nThe initial_value argument sets the value of object.  The newline\nargument is like the one of TextIOWrapper's constructor."
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __next__(self) -> typing.Any:
        'Implement next(self).'
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def close(self) -> typing.Any:
        'Close the IO object.\n\nAttempting any further operation after the object is closed\nwill raise a ValueError.\n\nThis method has no effect if the file is already closed.'
        ...
    
    @property
    def closed(self) -> typing.Any:
        ...
    
    def getvalue(self) -> typing.Any:
        'Retrieve the entire contents of the object.'
        ...
    
    @property
    def line_buffering(self) -> typing.Any:
        ...
    
    @property
    def newlines(self) -> typing.Any:
        ...
    
    def read(self, size) -> typing.Any:
        'Read at most size characters, returned as a string.\n\nIf the argument is negative or omitted, read until EOF\nis reached. Return an empty string at EOF.'
        ...
    
    def readable(self) -> typing.Any:
        'Returns True if the IO object can be read.'
        ...
    
    def readline(self, size) -> typing.Any:
        'Read until newline or EOF.\n\nReturns an empty string if EOF is hit immediately.'
        ...
    
    def seek(self, pos, whence) -> typing.Any:
        'Change stream position.\n\nSeek to character offset pos relative to position indicated by whence:\n    0  Start of stream (the default).  pos should be >= 0;\n    1  Current position - pos must be 0;\n    2  End of stream - pos must be 0.\nReturns the new absolute position.'
        ...
    
    def seekable(self) -> typing.Any:
        'Returns True if the IO object can be seeked.'
        ...
    
    def tell(self) -> typing.Any:
        'Tell the current file position.'
        ...
    
    def truncate(self, pos) -> typing.Any:
        'Truncate size to pos.\n\nThe pos argument defaults to the current file position, as\nreturned by tell().  The current file position is unchanged.\nReturns the new absolute position.'
        ...
    
    def writable(self) -> typing.Any:
        'Returns True if the IO object can be written.'
        ...
    
    def write(self, s) -> typing.Any:
        'Write string to file.\n\nReturns the number of characters written, which is always equal to\nthe length of the string.'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class TextIOWrapper(_TextIOBase):
    'Character and line based layer over a BufferedIOBase object, buffer.\n\nencoding gives the name of the encoding that the stream will be\ndecoded or encoded with. It defaults to locale.getpreferredencoding(False).\n\nerrors determines the strictness of encoding and decoding (see\nhelp(codecs.Codec) or the documentation for codecs.register) and\ndefaults to "strict".\n\nnewline controls how line endings are handled. It can be None, \'\',\n\'\\n\', \'\\r\', and \'\\r\\n\'.  It works as follows:\n\n* On input, if newline is None, universal newlines mode is\n  enabled. Lines in the input can end in \'\\n\', \'\\r\', or \'\\r\\n\', and\n  these are translated into \'\\n\' before being returned to the\n  caller. If it is \'\', universal newline mode is enabled, but line\n  endings are returned to the caller untranslated. If it has any of\n  the other legal values, input lines are only terminated by the given\n  string, and the line ending is returned to the caller untranslated.\n\n* On output, if newline is None, any \'\\n\' characters written are\n  translated to the system default line separator, os.linesep. If\n  newline is \'\' or \'\\n\', no translation takes place. If newline is any\n  of the other legal values, any \'\\n\' characters written are translated\n  to the given string.\n\nIf line_buffering is True, a call to flush is implied when a call to\nwrite contains a newline character.'
    @property
    def _CHUNK_SIZE(self) -> typing.Any:
        ...
    
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Character and line based layer over a BufferedIOBase object, buffer.\n\nencoding gives the name of the encoding that the stream will be\ndecoded or encoded with. It defaults to locale.getpreferredencoding(False).\n\nerrors determines the strictness of encoding and decoding (see\nhelp(codecs.Codec) or the documentation for codecs.register) and\ndefaults to "strict".\n\nnewline controls how line endings are handled. It can be None, \'\',\n\'\\n\', \'\\r\', and \'\\r\\n\'.  It works as follows:\n\n* On input, if newline is None, universal newlines mode is\n  enabled. Lines in the input can end in \'\\n\', \'\\r\', or \'\\r\\n\', and\n  these are translated into \'\\n\' before being returned to the\n  caller. If it is \'\', universal newline mode is enabled, but line\n  endings are returned to the caller untranslated. If it has any of\n  the other legal values, input lines are only terminated by the given\n  string, and the line ending is returned to the caller untranslated.\n\n* On output, if newline is None, any \'\\n\' characters written are\n  translated to the system default line separator, os.linesep. If\n  newline is \'\' or \'\\n\', no translation takes place. If newline is any\n  of the other legal values, any \'\\n\' characters written are translated\n  to the given string.\n\nIf line_buffering is True, a call to flush is implied when a call to\nwrite contains a newline character.'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __next__(self) -> typing.Any:
        'Implement next(self).'
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def _finalizing(self) -> typing.Any:
        ...
    
    @property
    def buffer(self) -> typing.Any:
        ...
    
    def close(self) -> typing.Any:
        ...
    
    @property
    def closed(self) -> typing.Any:
        ...
    
    def detach(self) -> typing.Any:
        ...
    
    @property
    def encoding(self) -> typing.Any:
        ...
    
    @property
    def errors(self) -> typing.Any:
        ...
    
    def fileno(self) -> typing.Any:
        ...
    
    def flush(self) -> typing.Any:
        ...
    
    def isatty(self) -> typing.Any:
        ...
    
    @property
    def line_buffering(self) -> typing.Any:
        ...
    
    @property
    def name(self) -> typing.Any:
        ...
    
    @property
    def newlines(self) -> typing.Any:
        ...
    
    def read(self, size) -> typing.Any:
        ...
    
    def readable(self) -> typing.Any:
        ...
    
    def readline(self, size) -> typing.Any:
        ...
    
    def reconfigure(self) -> typing.Any:
        'Reconfigure the text stream with new parameters.\n\nThis also does an implicit stream flush.'
        ...
    
    def seek(self, cookie, whence) -> typing.Any:
        ...
    
    def seekable(self) -> typing.Any:
        ...
    
    def tell(self) -> typing.Any:
        ...
    
    def truncate(self, pos) -> typing.Any:
        ...
    
    def writable(self) -> typing.Any:
        ...
    
    def write(self, text) -> typing.Any:
        ...
    
    @property
    def write_through(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

UnsupportedOperation = _mod_io.UnsupportedOperation
class _BufferedIOBase(_IOBase):
    'Base class for buffered IO objects.\n\nThe main difference with RawIOBase is that the read() method\nsupports omitting the size argument, and does not have a default\nimplementation that defers to readinto().\n\nIn addition, read(), readinto() and write() may raise\nBlockingIOError if the underlying raw stream is in non-blocking\nmode and not ready; unlike their raw counterparts, they will never\nreturn None.\n\nA typical implementation should not inherit from a RawIOBase\nimplementation, but wrap one.\n'
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Base class for buffered IO objects.\n\nThe main difference with RawIOBase is that the read() method\nsupports omitting the size argument, and does not have a default\nimplementation that defers to readinto().\n\nIn addition, read(), readinto() and write() may raise\nBlockingIOError if the underlying raw stream is in non-blocking\nmode and not ready; unlike their raw counterparts, they will never\nreturn None.\n\nA typical implementation should not inherit from a RawIOBase\nimplementation, but wrap one.\n'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def detach(self) -> typing.Any:
        'Disconnect this buffer from its underlying raw stream and return it.\n\nAfter the raw stream has been detached, the buffer is in an unusable\nstate.'
        ...
    
    def read(self) -> typing.Any:
        "Read and return up to n bytes.\n\nIf the argument is omitted, None, or negative, reads and\nreturns all data until EOF.\n\nIf the argument is positive, and the underlying raw stream is\nnot 'interactive', multiple raw reads may be issued to satisfy\nthe byte count (unless EOF is reached first).  But for\ninteractive raw streams (as well as sockets and pipes), at most\none raw read will be issued, and a short result does not imply\nthat EOF is imminent.\n\nReturns an empty bytes object on EOF.\n\nReturns None if the underlying raw stream was open in non-blocking\nmode and no data is available at the moment.\n"
        ...
    
    def read1(self) -> typing.Any:
        'Read and return up to n bytes, with at most one read() call\nto the underlying raw stream. A short result does not imply\nthat EOF is imminent.\n\nReturns an empty bytes object on EOF.\n'
        ...
    
    def readinto(self, buffer) -> typing.Any:
        ...
    
    def readinto1(self, buffer) -> typing.Any:
        ...
    
    def write(self) -> typing.Any:
        'Write the given buffer to the IO stream.\n\nReturns the number of bytes written, which is always the length of b\nin bytes.\n\nRaises BlockingIOError if the buffer is full and the\nunderlying raw stream cannot accept more data at the moment.\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _IOBase(_mod_builtins.object):
    "The abstract base class for all I/O classes.\n\nThis class provides dummy implementations for many methods that\nderived classes can override selectively; the default implementations\nrepresent a file that cannot be read, written or seeked.\n\nEven though IOBase does not declare read, readinto, or write because\ntheir signatures will vary, implementations and clients should\nconsider those methods part of the interface. Also, implementations\nmay raise UnsupportedOperation when operations they do not support are\ncalled.\n\nThe basic type used for binary data read from or written to a file is\nbytes. Other bytes-like objects are accepted as method arguments too.\nIn some cases (such as readinto), a writable object is required. Text\nI/O classes work with str data.\n\nNote that calling any method (except additional calls to close(),\nwhich are ignored) on a closed stream should raise a ValueError.\n\nIOBase (and its subclasses) support the iterator protocol, meaning\nthat an IOBase object can be iterated over yielding the lines in a\nstream.\n\nIOBase also supports the :keyword:`with` statement. In this example,\nfp is closed after the suite of the with statement is complete:\n\nwith open('spam.txt', 'r') as fp:\n    fp.write('Spam and eggs!')\n"
    def __del__(self) -> None:
        ...
    
    __dict__: typing.Dict[str, typing.Any]
    def __enter__(self) -> typing.Any:
        ...
    
    def __exit__(self) -> typing.Any:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        "The abstract base class for all I/O classes.\n\nThis class provides dummy implementations for many methods that\nderived classes can override selectively; the default implementations\nrepresent a file that cannot be read, written or seeked.\n\nEven though IOBase does not declare read, readinto, or write because\ntheir signatures will vary, implementations and clients should\nconsider those methods part of the interface. Also, implementations\nmay raise UnsupportedOperation when operations they do not support are\ncalled.\n\nThe basic type used for binary data read from or written to a file is\nbytes. Other bytes-like objects are accepted as method arguments too.\nIn some cases (such as readinto), a writable object is required. Text\nI/O classes work with str data.\n\nNote that calling any method (except additional calls to close(),\nwhich are ignored) on a closed stream should raise a ValueError.\n\nIOBase (and its subclasses) support the iterator protocol, meaning\nthat an IOBase object can be iterated over yielding the lines in a\nstream.\n\nIOBase also supports the :keyword:`with` statement. In this example,\nfp is closed after the suite of the with statement is complete:\n\nwith open('spam.txt', 'r') as fp:\n    fp.write('Spam and eggs!')\n"
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __iter__(self) -> _IOBase:
        'Implement iter(self).'
        ...
    
    def __next__(self) -> typing.Any:
        'Implement next(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _checkClosed(self) -> typing.Any:
        ...
    
    def _checkReadable(self) -> typing.Any:
        ...
    
    def _checkSeekable(self) -> typing.Any:
        ...
    
    def _checkWritable(self) -> typing.Any:
        ...
    
    def close(self) -> typing.Any:
        'Flush and close the IO object.\n\nThis method has no effect if the file is already closed.'
        ...
    
    @property
    def closed(self) -> typing.Any:
        ...
    
    def fileno(self) -> typing.Any:
        'Returns underlying file descriptor if one exists.\n\nOSError is raised if the IO object does not use a file descriptor.'
        ...
    
    def flush(self) -> typing.Any:
        'Flush write buffers, if applicable.\n\nThis is not implemented for read-only and non-blocking streams.'
        ...
    
    def isatty(self) -> typing.Any:
        "Return whether this is an 'interactive' stream.\n\nReturn False if it can't be determined."
        ...
    
    def readable(self) -> typing.Any:
        'Return whether object was opened for reading.\n\nIf False, read() will raise OSError.'
        ...
    
    def readline(self, size) -> typing.Any:
        "Read and return a line from the stream.\n\nIf size is specified, at most size bytes will be read.\n\nThe line terminator is always b'\\n' for binary files; for text\nfiles, the newlines argument to open can be used to select the line\nterminator(s) recognized."
        ...
    
    def readlines(self, hint) -> typing.Any:
        'Return a list of lines from the stream.\n\nhint can be specified to control the number of lines read: no more\nlines will be read if the total size (in bytes/characters) of all\nlines so far exceeds hint.'
        ...
    
    def seek(self) -> typing.Any:
        'Change stream position.\n\nChange the stream position to the given byte offset. The offset is\ninterpreted relative to the position indicated by whence.  Values\nfor whence are:\n\n* 0 -- start of stream (the default); offset should be zero or positive\n* 1 -- current stream position; offset may be negative\n* 2 -- end of stream; offset is usually negative\n\nReturn the new absolute position.'
        ...
    
    def seekable(self) -> typing.Any:
        'Return whether object supports random access.\n\nIf False, seek(), tell() and truncate() will raise OSError.\nThis method may need to do a test seek().'
        ...
    
    def tell(self) -> typing.Any:
        'Return current stream position.'
        ...
    
    def truncate(self) -> typing.Any:
        'Truncate file to size bytes.\n\nFile pointer is left unchanged.  Size defaults to the current IO\nposition as reported by tell().  Returns the new size.'
        ...
    
    def writable(self) -> typing.Any:
        'Return whether object was opened for writing.\n\nIf False, write() will raise OSError.'
        ...
    
    def writelines(self, lines) -> typing.Any:
        'Write a list of lines to stream.\n\nLine separators are not added, so it is usual for each of the\nlines provided to have a line separator at the end.'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _RawIOBase(_IOBase):
    'Base class for raw binary I/O.'
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Base class for raw binary I/O.'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def read(self, size) -> typing.Any:
        ...
    
    def readall(self) -> typing.Any:
        'Read until EOF, using multiple read() call.'
        ...
    
    def readinto(self) -> typing.Any:
        ...
    
    def write(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _TextIOBase(_IOBase):
    "Base class for text I/O.\n\nThis class provides a character and line based interface to stream\nI/O. There is no readinto method because Python's character strings\nare immutable.\n"
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        "Base class for text I/O.\n\nThis class provides a character and line based interface to stream\nI/O. There is no readinto method because Python's character strings\nare immutable.\n"
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def detach(self) -> typing.Any:
        'Separate the underlying buffer from the TextIOBase and return it.\n\nAfter the underlying buffer has been detached, the TextIO is in an\nunusable state.\n'
        ...
    
    @property
    def encoding(self) -> typing.Any:
        'Encoding of the text stream.\n\nSubclasses should override.\n'
        ...
    
    @property
    def errors(self) -> typing.Any:
        'The error setting of the decoder or encoder.\n\nSubclasses should override.\n'
        ...
    
    @property
    def newlines(self) -> typing.Any:
        'Line endings translated so far.\n\nOnly line endings translated during reading are considered.\n\nSubclasses should override.\n'
        ...
    
    def read(self) -> typing.Any:
        'Read at most n characters from stream.\n\nRead from underlying buffer until we have n characters or we hit EOF.\nIf n is negative or omitted, read until EOF.\n'
        ...
    
    def readline(self) -> typing.Any:
        'Read until newline or EOF.\n\nReturns an empty string if EOF is hit immediately.\n'
        ...
    
    def write(self) -> typing.Any:
        'Write string to stream.\nReturns the number of characters written (which is always equal to\nthe length of the string).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _WindowsConsoleIO(_RawIOBase):
    "Open a console buffer by file descriptor.\n\nThe mode can be 'rb' (default), or 'wb' for reading or writing bytes. All\nother mode characters will be ignored. Mode 'b' will be assumed if it is\nomitted. The *opener* parameter is always ignored."
    __dict__: typing.Dict[str, typing.Any]
    def __getattribute__(self, name) -> typing.Any:
        'Return getattr(self, name).'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        "Open a console buffer by file descriptor.\n\nThe mode can be 'rb' (default), or 'wb' for reading or writing bytes. All\nother mode characters will be ignored. Mode 'b' will be assumed if it is\nomitted. The *opener* parameter is always ignored."
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def _blksize(self) -> typing.Any:
        ...
    
    @property
    def _finalizing(self) -> typing.Any:
        ...
    
    def close(self) -> typing.Any:
        'Close the console object.\n\nA closed console object cannot be used for further I/O operations.\nclose() may be called more than once without error.'
        ...
    
    @property
    def closed(self) -> typing.Any:
        'True if the file is closed'
        ...
    
    @property
    def closefd(self) -> typing.Any:
        'True if the file descriptor will be closed by close().'
        ...
    
    def fileno(self) -> typing.Any:
        'Return the underlying file descriptor (an integer).'
        ...
    
    def isatty(self) -> typing.Any:
        'Always True.'
        ...
    
    @property
    def mode(self) -> typing.Any:
        'String giving the file mode'
        ...
    
    def read(self, size) -> typing.Any:
        'Read at most size bytes, returned as bytes.\n\nOnly makes one system call when size is a positive integer,\nso less data may be returned than requested.\nReturn an empty bytes object at EOF.'
        ...
    
    def readable(self) -> typing.Any:
        'True if console is an input buffer.'
        ...
    
    def readall(self) -> typing.Any:
        'Read all data from the console, returned as bytes.\n\nReturn an empty bytes object at EOF.'
        ...
    
    def readinto(self, buffer) -> typing.Any:
        'Same as RawIOBase.readinto().'
        ...
    
    def writable(self) -> typing.Any:
        'True if console is an output buffer.'
        ...
    
    def write(self, b) -> typing.Any:
        'Write buffer b to file, return number of bytes written.\n\nOnly makes one system call, so not all of the data may be written.\nThe number of bytes actually written is returned.'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: str
__name__: str
__package__: str
def open(file, mode, buffering, encoding, errors, newline, closefd, opener) -> typing.Any:
    'Open file and return a stream.  Raise OSError upon failure.\n\nfile is either a text or byte string giving the name (and the path\nif the file isn\'t in the current working directory) of the file to\nbe opened or an integer file descriptor of the file to be\nwrapped. (If a file descriptor is given, it is closed when the\nreturned I/O object is closed, unless closefd is set to False.)\n\nmode is an optional string that specifies the mode in which the file\nis opened. It defaults to \'r\' which means open for reading in text\nmode.  Other common values are \'w\' for writing (truncating the file if\nit already exists), \'x\' for creating and writing to a new file, and\n\'a\' for appending (which on some Unix systems, means that all writes\nappend to the end of the file regardless of the current seek position).\nIn text mode, if encoding is not specified the encoding used is platform\ndependent: locale.getpreferredencoding(False) is called to get the\ncurrent locale encoding. (For reading and writing raw bytes use binary\nmode and leave encoding unspecified.) The available modes are:\n\n========= ===============================================================\nCharacter Meaning\n--------- ---------------------------------------------------------------\n\'r\'       open for reading (default)\n\'w\'       open for writing, truncating the file first\n\'x\'       create a new file and open it for writing\n\'a\'       open for writing, appending to the end of the file if it exists\n\'b\'       binary mode\n\'t\'       text mode (default)\n\'+\'       open a disk file for updating (reading and writing)\n\'U\'       universal newline mode (deprecated)\n========= ===============================================================\n\nThe default mode is \'rt\' (open for reading text). For binary random\naccess, the mode \'w+b\' opens and truncates the file to 0 bytes, while\n\'r+b\' opens the file without truncation. The \'x\' mode implies \'w\' and\nraises an `FileExistsError` if the file already exists.\n\nPython distinguishes between files opened in binary and text modes,\neven when the underlying operating system doesn\'t. Files opened in\nbinary mode (appending \'b\' to the mode argument) return contents as\nbytes objects without any decoding. In text mode (the default, or when\n\'t\' is appended to the mode argument), the contents of the file are\nreturned as strings, the bytes having been first decoded using a\nplatform-dependent encoding or using the specified encoding if given.\n\n\'U\' mode is deprecated and will raise an exception in future versions\nof Python.  It has no effect in Python 3.  Use newline to control\nuniversal newlines mode.\n\nbuffering is an optional integer used to set the buffering policy.\nPass 0 to switch buffering off (only allowed in binary mode), 1 to select\nline buffering (only usable in text mode), and an integer > 1 to indicate\nthe size of a fixed-size chunk buffer.  When no buffering argument is\ngiven, the default buffering policy works as follows:\n\n* Binary files are buffered in fixed-size chunks; the size of the buffer\n  is chosen using a heuristic trying to determine the underlying device\'s\n  "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.\n  On many systems, the buffer will typically be 4096 or 8192 bytes long.\n\n* "Interactive" text files (files for which isatty() returns True)\n  use line buffering.  Other text files use the policy described above\n  for binary files.\n\nencoding is the name of the encoding used to decode or encode the\nfile. This should only be used in text mode. The default encoding is\nplatform dependent, but any encoding supported by Python can be\npassed.  See the codecs module for the list of supported encodings.\n\nerrors is an optional string that specifies how encoding errors are to\nbe handled---this argument should not be used in binary mode. Pass\n\'strict\' to raise a ValueError exception if there is an encoding error\n(the default of None has the same effect), or pass \'ignore\' to ignore\nerrors. (Note that ignoring encoding errors can lead to data loss.)\nSee the documentation for codecs.register or run \'help(codecs.Codec)\'\nfor a list of the permitted encoding error strings.\n\nnewline controls how universal newlines works (it only applies to text\nmode). It can be None, \'\', \'\\n\', \'\\r\', and \'\\r\\n\'.  It works as\nfollows:\n\n* On input, if newline is None, universal newlines mode is\n  enabled. Lines in the input can end in \'\\n\', \'\\r\', or \'\\r\\n\', and\n  these are translated into \'\\n\' before being returned to the\n  caller. If it is \'\', universal newline mode is enabled, but line\n  endings are returned to the caller untranslated. If it has any of\n  the other legal values, input lines are only terminated by the given\n  string, and the line ending is returned to the caller untranslated.\n\n* On output, if newline is None, any \'\\n\' characters written are\n  translated to the system default line separator, os.linesep. If\n  newline is \'\' or \'\\n\', no translation takes place. If newline is any\n  of the other legal values, any \'\\n\' characters written are translated\n  to the given string.\n\nIf closefd is False, the underlying file descriptor will be kept open\nwhen the file is closed. This does not work when a file name is given\nand must be True in that case.\n\nA custom opener can be used by passing a callable as *opener*. The\nunderlying file descriptor for the file object is then obtained by\ncalling *opener* with (*file*, *flags*). *opener* must return an open\nfile descriptor (passing os.open as *opener* results in functionality\nsimilar to passing None).\n\nopen() returns a file object whose type depends on the mode, and\nthrough which the standard file operations such as reading and writing\nare performed. When open() is used to open a file in a text mode (\'w\',\n\'r\', \'wt\', \'rt\', etc.), it returns a TextIOWrapper. When used to open\na file in a binary mode, the returned class varies: in read binary\nmode, it returns a BufferedReader; in write binary and append binary\nmodes, it returns a BufferedWriter, and in read/write mode, it returns\na BufferedRandom.\n\nIt is also possible to use a string or bytearray as a file for both\nreading and writing. For strings StringIO can be used like a file\nopened in a text mode, and for bytes a BytesIO can be used like a file\nopened in a binary mode.'
    ...

def open_code(path) -> typing.Any:
    "Opens the provided file with the intent to import the contents.\n\nThis may perform extra validation beyond open(), but is otherwise interchangeable\nwith calling open(path, 'rb')."
    ...

def text_encoding(encoding, stacklevel) -> typing.Any:
    'A helper function to choose the text encoding.\n\nWhen encoding is not None, just return it.\nOtherwise, return the default text encoding (i.e. "locale").\n\nThis function emits an EncodingWarning if encoding is None and\nsys.flags.warn_default_encoding is true.\n\nThis can be used in APIs with an encoding=None parameter.\nHowever, please consider using encoding="utf-8" for new APIs.'
    ...

def __getattr__(name) -> typing.Any:
    ...

