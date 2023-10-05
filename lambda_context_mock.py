import uuid


def lambda_context():
    class LambdaContext:
        def __init__(self):
            self.function_name = "test-func"
            self.function_version = "$LATEST"
            self.memory_limit_in_mb = 128
            self.invoked_function_arn = "arn:aws:lambda:eu-west-1:809313241234:function:test-func"
            self.aws_request_id = uuid.uuid4()
            self.log_group_name = "teste"
            self.log_stream_name = "teste"

        def get_remaining_time_in_millis(self) -> int:
            return 1000

    return LambdaContext()