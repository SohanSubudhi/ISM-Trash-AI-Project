
import filetype

def what(file, h=None):
    """
    Clone of imghdr.what using filetype library.
    """
    try:
        if h:
            # If bytes are provided directly
            kind = filetype.guess(h)
        else:
            # If a filename is provided
            kind = filetype.guess(file)
            
        if kind:
            return kind.extension
        return None
    except Exception:
        return None
