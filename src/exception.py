import sys
import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Build a detailed error message with file name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    return (
        f"Error occurred in python script [{file_name}] "
        f"line number [{exc_tb.tb_lineno}] "
        f"error message [{error}]"
    )

class CustomException(Exception):
    def __init__(self, error: Exception, error_detail: sys):
        super().__init__(str(error))
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self) -> str:
        return self.error_message
