# class HelmException(Exception):
#     def __init__(self, message='Generic Exception'):
#         super().__init__(message)

class CommandExecutionError(Exception):
    def __init__(self, rc, out):
        self.return_code = rc
        self.error_output = out
        super().__init__(f"Command execution failed with rc {rc}: {out}")
