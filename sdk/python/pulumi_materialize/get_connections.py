# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetConnectionsResult',
    'AwaitableGetConnectionsResult',
    'get_connections',
    'get_connections_output',
]

@pulumi.output_type
class GetConnectionsResult:
    """
    A collection of values returned by GetConnections.
    """
    def __init__(__self__, connections=None, database_name=None, id=None, schema_name=None):
        if connections and not isinstance(connections, list):
            raise TypeError("Expected argument 'connections' to be a list")
        pulumi.set(__self__, "connections", connections)
        if database_name and not isinstance(database_name, str):
            raise TypeError("Expected argument 'database_name' to be a str")
        pulumi.set(__self__, "database_name", database_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if schema_name and not isinstance(schema_name, str):
            raise TypeError("Expected argument 'schema_name' to be a str")
        pulumi.set(__self__, "schema_name", schema_name)

    @property
    @pulumi.getter
    def connections(self) -> Sequence['outputs.GetConnectionsConnectionResult']:
        """
        The schemas in the account
        """
        return pulumi.get(self, "connections")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[str]:
        """
        Limit connections to a specific database
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[str]:
        """
        Limit connections to a specific schema within a specific database
        """
        return pulumi.get(self, "schema_name")


class AwaitableGetConnectionsResult(GetConnectionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConnectionsResult(
            connections=self.connections,
            database_name=self.database_name,
            id=self.id,
            schema_name=self.schema_name)


def get_connections(database_name: Optional[str] = None,
                    schema_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConnectionsResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_materialize as materialize

    all = materialize.get_connections()
    materialize = materialize.get_connections(database_name="materialize")
    materialize_schema = materialize.get_connections(database_name="materialize",
        schema_name="schema")
    ```


    :param str database_name: Limit connections to a specific database
    :param str schema_name: Limit connections to a specific schema within a specific database
    """
    __args__ = dict()
    __args__['databaseName'] = database_name
    __args__['schemaName'] = schema_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('materialize:index/getConnections:GetConnections', __args__, opts=opts, typ=GetConnectionsResult).value

    return AwaitableGetConnectionsResult(
        connections=__ret__.connections,
        database_name=__ret__.database_name,
        id=__ret__.id,
        schema_name=__ret__.schema_name)


@_utilities.lift_output_func(get_connections)
def get_connections_output(database_name: Optional[pulumi.Input[Optional[str]]] = None,
                           schema_name: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConnectionsResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_materialize as materialize

    all = materialize.get_connections()
    materialize = materialize.get_connections(database_name="materialize")
    materialize_schema = materialize.get_connections(database_name="materialize",
        schema_name="schema")
    ```


    :param str database_name: Limit connections to a specific database
    :param str schema_name: Limit connections to a specific schema within a specific database
    """
    ...