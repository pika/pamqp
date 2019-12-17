"""
AMQP Exceptions
===============

Auto-generated, do not edit. To Generate run `.tools/codegen.py`

"""


class PAMQPException(Exception):
    """Base exception for all pamqp specific exceptions."""


class UnmarshalingException(PAMQPException):
    """Raised when a frame is not able to be unmarshaled."""
    def __str__(self):  # pragma: nocover
        return 'Could not unmarshal {} frame: {}'.format(
            self.args[0], self.args[1])


class AMQPError(PAMQPException):
    """Base exception for all AMQP errors."""


class AMQPSoftError(AMQPError):
    """Base exception for all AMQP soft errors."""


class AMQPHardError(AMQPError):
    """Base exception for all AMQP hard errors."""


class AMQPContentTooLarge(AMQPSoftError):
    """
    The client attempted to transfer content larger than the server could
    accept at the present time. The client may retry at a later time.

    """
    name = 'CONTENT-TOO-LARGE'
    value = 311


class AMQPNoRoute(AMQPSoftError):
    """
    Undocumented AMQP Soft Error

    """
    name = 'NO-ROUTE'
    value = 312


class AMQPNoConsumers(AMQPSoftError):
    """
    When the exchange cannot deliver to a consumer when the immediate flag is
    set. As a result of pending data on the queue or the absence of any
    consumers of the queue.

    """
    name = 'NO-CONSUMERS'
    value = 313


class AMQPAccessRefused(AMQPSoftError):
    """
    The client attempted to work with a server entity to which it has no access
    due to security settings.

    """
    name = 'ACCESS-REFUSED'
    value = 403


class AMQPNotFound(AMQPSoftError):
    """
    The client attempted to work with a server entity that does not exist.

    """
    name = 'NOT-FOUND'
    value = 404


class AMQPResourceLocked(AMQPSoftError):
    """
    The client attempted to work with a server entity to which it has no access
    because another client is working with it.

    """
    name = 'RESOURCE-LOCKED'
    value = 405


class AMQPPreconditionFailed(AMQPSoftError):
    """
    The client requested a method that was not allowed because some
    precondition failed.

    """
    name = 'PRECONDITION-FAILED'
    value = 406


class AMQPConnectionForced(AMQPHardError):
    """
    An operator intervened to close the connection for some reason. The client
    may retry at some later date.

    """
    name = 'CONNECTION-FORCED'
    value = 320


class AMQPInvalidPath(AMQPHardError):
    """
    The client tried to work with an unknown virtual host.

    """
    name = 'INVALID-PATH'
    value = 402


class AMQPFrameError(AMQPHardError):
    """
    The sender sent a malformed frame that the recipient could not decode. This
    strongly implies a programming error in the sending peer.

    """
    name = 'FRAME-ERROR'
    value = 501


class AMQPSyntaxError(AMQPHardError):
    """
    The sender sent a frame that contained illegal values for one or more
    fields. This strongly implies a programming error in the sending peer.

    """
    name = 'SYNTAX-ERROR'
    value = 502


class AMQPCommandInvalid(AMQPHardError):
    """
    The client sent an invalid sequence of frames, attempting to perform an
    operation that was considered invalid by the server. This usually implies a
    programming error in the client.

    """
    name = 'COMMAND-INVALID'
    value = 503


class AMQPChannelError(AMQPHardError):
    """
    The client attempted to work with a channel that had not been correctly
    opened. This most likely indicates a fault in the client layer.

    """
    name = 'CHANNEL-ERROR'
    value = 504


class AMQPUnexpectedFrame(AMQPHardError):
    """
    The peer sent a frame that was not expected, usually in the context of a
    content header and body.  This strongly indicates a fault in the peer's
    content processing.

    """
    name = 'UNEXPECTED-FRAME'
    value = 505


class AMQPResourceError(AMQPHardError):
    """
    The server could not complete the method because it lacked sufficient
    resources. This may be due to the client creating too many of some type of
    entity.

    """
    name = 'RESOURCE-ERROR'
    value = 506


class AMQPNotAllowed(AMQPHardError):
    """
    The client tried to work with some entity in a manner that is prohibited by
    the server, due to security settings or by some other criteria.

    """
    name = 'NOT-ALLOWED'
    value = 530


class AMQPNotImplemented(AMQPHardError):
    """
    The client tried to use functionality that is not implemented in the
    server.

    """
    name = 'NOT-IMPLEMENTED'
    value = 540


class AMQPInternalError(AMQPHardError):
    """
    The server could not complete the method because of an internal error. The
    server may require intervention by an operator in order to resume normal
    operations.

    """
    name = 'INTERNAL-ERROR'
    value = 541


# AMQP Error code to class mapping
CLASS_MAPPING = {
    311: AMQPContentTooLarge,
    312: AMQPNoRoute,
    313: AMQPNoConsumers,
    403: AMQPAccessRefused,
    404: AMQPNotFound,
    405: AMQPResourceLocked,
    406: AMQPPreconditionFailed,
    320: AMQPConnectionForced,
    402: AMQPInvalidPath,
    501: AMQPFrameError,
    502: AMQPSyntaxError,
    503: AMQPCommandInvalid,
    504: AMQPChannelError,
    505: AMQPUnexpectedFrame,
    506: AMQPResourceError,
    530: AMQPNotAllowed,
    540: AMQPNotImplemented,
    541: AMQPInternalError
}
