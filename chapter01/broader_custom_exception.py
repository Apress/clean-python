class WrongInstanceIDError(Exception):
    """Raise the exception whenever Invalid instance found."""
    def __init__(self, message=None, errros=None):
        # Calling the base class constructor with the parameter it needs
        super().__init__(message)
        # New for your custom code
        self.errors = errors


ec2 = session.get_client('ec2', 'us-east-2')
try:
    parsed = ec2.describe_instances(InstanceIds=['i-badid'])
except ClientError as e:
    logger.error("Received error: %s", e, exc_info=True)
    # Only worry about a specific service error code
    if e.response['Error']['Code'] == 'InvalidInstanceID.NotFound':
        raise WrongInstanceIDError(message=exc_info, errors=e)
