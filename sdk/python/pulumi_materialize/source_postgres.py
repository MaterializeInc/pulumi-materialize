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
from ._inputs import *

__all__ = ['SourcePostgresArgs', 'SourcePostgres']

@pulumi.input_type
class SourcePostgresArgs:
    def __init__(__self__, *,
                 postgres_connection: pulumi.Input['SourcePostgresPostgresConnectionArgs'],
                 publication: pulumi.Input[str],
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 tables: Optional[pulumi.Input[Sequence[pulumi.Input['SourcePostgresTableArgs']]]] = None,
                 text_columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SourcePostgres resource.
        :param pulumi.Input['SourcePostgresPostgresConnectionArgs'] postgres_connection: The PostgreSQL connection to use in the source.
        :param pulumi.Input[str] publication: The PostgreSQL publication (the replication data set containing the tables to be streamed to Materialize).
        :param pulumi.Input[str] cluster_name: The cluster to maintain this source. If not specified, the size option must be specified.
        :param pulumi.Input[str] database_name: The identifier for the source database.
        :param pulumi.Input[str] name: The identifier for the source.
        :param pulumi.Input[str] schema_name: The identifier for the source schema.
        :param pulumi.Input[str] size: The size of the source.
        :param pulumi.Input[Sequence[pulumi.Input['SourcePostgresTableArgs']]] tables: Creates subsources for specific tables.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] text_columns: Decode data as text for specific columns that contain PostgreSQL types that are unsupported in Materialize.
        """
        pulumi.set(__self__, "postgres_connection", postgres_connection)
        pulumi.set(__self__, "publication", publication)
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if schema_name is not None:
            pulumi.set(__self__, "schema_name", schema_name)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if tables is not None:
            pulumi.set(__self__, "tables", tables)
        if text_columns is not None:
            pulumi.set(__self__, "text_columns", text_columns)

    @property
    @pulumi.getter(name="postgresConnection")
    def postgres_connection(self) -> pulumi.Input['SourcePostgresPostgresConnectionArgs']:
        """
        The PostgreSQL connection to use in the source.
        """
        return pulumi.get(self, "postgres_connection")

    @postgres_connection.setter
    def postgres_connection(self, value: pulumi.Input['SourcePostgresPostgresConnectionArgs']):
        pulumi.set(self, "postgres_connection", value)

    @property
    @pulumi.getter
    def publication(self) -> pulumi.Input[str]:
        """
        The PostgreSQL publication (the replication data set containing the tables to be streamed to Materialize).
        """
        return pulumi.get(self, "publication")

    @publication.setter
    def publication(self, value: pulumi.Input[str]):
        pulumi.set(self, "publication", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        The cluster to maintain this source. If not specified, the size option must be specified.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the source database.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the source.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the source schema.
        """
        return pulumi.get(self, "schema_name")

    @schema_name.setter
    def schema_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_name", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        """
        The size of the source.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def tables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SourcePostgresTableArgs']]]]:
        """
        Creates subsources for specific tables.
        """
        return pulumi.get(self, "tables")

    @tables.setter
    def tables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SourcePostgresTableArgs']]]]):
        pulumi.set(self, "tables", value)

    @property
    @pulumi.getter(name="textColumns")
    def text_columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Decode data as text for specific columns that contain PostgreSQL types that are unsupported in Materialize.
        """
        return pulumi.get(self, "text_columns")

    @text_columns.setter
    def text_columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "text_columns", value)


@pulumi.input_type
class _SourcePostgresState:
    def __init__(__self__, *,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 postgres_connection: Optional[pulumi.Input['SourcePostgresPostgresConnectionArgs']] = None,
                 publication: Optional[pulumi.Input[str]] = None,
                 qualified_sql_name: Optional[pulumi.Input[str]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 tables: Optional[pulumi.Input[Sequence[pulumi.Input['SourcePostgresTableArgs']]]] = None,
                 text_columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering SourcePostgres resources.
        :param pulumi.Input[str] cluster_name: The cluster to maintain this source. If not specified, the size option must be specified.
        :param pulumi.Input[str] database_name: The identifier for the source database.
        :param pulumi.Input[str] name: The identifier for the source.
        :param pulumi.Input['SourcePostgresPostgresConnectionArgs'] postgres_connection: The PostgreSQL connection to use in the source.
        :param pulumi.Input[str] publication: The PostgreSQL publication (the replication data set containing the tables to be streamed to Materialize).
        :param pulumi.Input[str] qualified_sql_name: The fully qualified name of the source.
        :param pulumi.Input[str] schema_name: The identifier for the source schema.
        :param pulumi.Input[str] size: The size of the source.
        :param pulumi.Input[str] source_type: The type of source.
        :param pulumi.Input[Sequence[pulumi.Input['SourcePostgresTableArgs']]] tables: Creates subsources for specific tables.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] text_columns: Decode data as text for specific columns that contain PostgreSQL types that are unsupported in Materialize.
        """
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if postgres_connection is not None:
            pulumi.set(__self__, "postgres_connection", postgres_connection)
        if publication is not None:
            pulumi.set(__self__, "publication", publication)
        if qualified_sql_name is not None:
            pulumi.set(__self__, "qualified_sql_name", qualified_sql_name)
        if schema_name is not None:
            pulumi.set(__self__, "schema_name", schema_name)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if source_type is not None:
            pulumi.set(__self__, "source_type", source_type)
        if tables is not None:
            pulumi.set(__self__, "tables", tables)
        if text_columns is not None:
            pulumi.set(__self__, "text_columns", text_columns)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        The cluster to maintain this source. If not specified, the size option must be specified.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the source database.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the source.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="postgresConnection")
    def postgres_connection(self) -> Optional[pulumi.Input['SourcePostgresPostgresConnectionArgs']]:
        """
        The PostgreSQL connection to use in the source.
        """
        return pulumi.get(self, "postgres_connection")

    @postgres_connection.setter
    def postgres_connection(self, value: Optional[pulumi.Input['SourcePostgresPostgresConnectionArgs']]):
        pulumi.set(self, "postgres_connection", value)

    @property
    @pulumi.getter
    def publication(self) -> Optional[pulumi.Input[str]]:
        """
        The PostgreSQL publication (the replication data set containing the tables to be streamed to Materialize).
        """
        return pulumi.get(self, "publication")

    @publication.setter
    def publication(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "publication", value)

    @property
    @pulumi.getter(name="qualifiedSqlName")
    def qualified_sql_name(self) -> Optional[pulumi.Input[str]]:
        """
        The fully qualified name of the source.
        """
        return pulumi.get(self, "qualified_sql_name")

    @qualified_sql_name.setter
    def qualified_sql_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "qualified_sql_name", value)

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the source schema.
        """
        return pulumi.get(self, "schema_name")

    @schema_name.setter
    def schema_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_name", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        """
        The size of the source.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of source.
        """
        return pulumi.get(self, "source_type")

    @source_type.setter
    def source_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_type", value)

    @property
    @pulumi.getter
    def tables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SourcePostgresTableArgs']]]]:
        """
        Creates subsources for specific tables.
        """
        return pulumi.get(self, "tables")

    @tables.setter
    def tables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SourcePostgresTableArgs']]]]):
        pulumi.set(self, "tables", value)

    @property
    @pulumi.getter(name="textColumns")
    def text_columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Decode data as text for specific columns that contain PostgreSQL types that are unsupported in Materialize.
        """
        return pulumi.get(self, "text_columns")

    @text_columns.setter
    def text_columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "text_columns", value)


class SourcePostgres(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 postgres_connection: Optional[pulumi.Input[pulumi.InputType['SourcePostgresPostgresConnectionArgs']]] = None,
                 publication: Optional[pulumi.Input[str]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 tables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SourcePostgresTableArgs']]]]] = None,
                 text_columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        A source describes an external system you want Materialize to read data from, and provides details about how to decode and interpret that data.

        ## Import

        # Sources can be imported using the source id

        ```sh
         $ pulumi import materialize:index/sourcePostgres:SourcePostgres example_source_postgres <source_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The cluster to maintain this source. If not specified, the size option must be specified.
        :param pulumi.Input[str] database_name: The identifier for the source database.
        :param pulumi.Input[str] name: The identifier for the source.
        :param pulumi.Input[pulumi.InputType['SourcePostgresPostgresConnectionArgs']] postgres_connection: The PostgreSQL connection to use in the source.
        :param pulumi.Input[str] publication: The PostgreSQL publication (the replication data set containing the tables to be streamed to Materialize).
        :param pulumi.Input[str] schema_name: The identifier for the source schema.
        :param pulumi.Input[str] size: The size of the source.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SourcePostgresTableArgs']]]] tables: Creates subsources for specific tables.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] text_columns: Decode data as text for specific columns that contain PostgreSQL types that are unsupported in Materialize.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SourcePostgresArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A source describes an external system you want Materialize to read data from, and provides details about how to decode and interpret that data.

        ## Import

        # Sources can be imported using the source id

        ```sh
         $ pulumi import materialize:index/sourcePostgres:SourcePostgres example_source_postgres <source_id>
        ```

        :param str resource_name: The name of the resource.
        :param SourcePostgresArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SourcePostgresArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 postgres_connection: Optional[pulumi.Input[pulumi.InputType['SourcePostgresPostgresConnectionArgs']]] = None,
                 publication: Optional[pulumi.Input[str]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 tables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SourcePostgresTableArgs']]]]] = None,
                 text_columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SourcePostgresArgs.__new__(SourcePostgresArgs)

            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["database_name"] = database_name
            __props__.__dict__["name"] = name
            if postgres_connection is None and not opts.urn:
                raise TypeError("Missing required property 'postgres_connection'")
            __props__.__dict__["postgres_connection"] = postgres_connection
            if publication is None and not opts.urn:
                raise TypeError("Missing required property 'publication'")
            __props__.__dict__["publication"] = publication
            __props__.__dict__["schema_name"] = schema_name
            __props__.__dict__["size"] = size
            __props__.__dict__["tables"] = tables
            __props__.__dict__["text_columns"] = text_columns
            __props__.__dict__["qualified_sql_name"] = None
            __props__.__dict__["source_type"] = None
        super(SourcePostgres, __self__).__init__(
            'materialize:index/sourcePostgres:SourcePostgres',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_name: Optional[pulumi.Input[str]] = None,
            database_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            postgres_connection: Optional[pulumi.Input[pulumi.InputType['SourcePostgresPostgresConnectionArgs']]] = None,
            publication: Optional[pulumi.Input[str]] = None,
            qualified_sql_name: Optional[pulumi.Input[str]] = None,
            schema_name: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[str]] = None,
            source_type: Optional[pulumi.Input[str]] = None,
            tables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SourcePostgresTableArgs']]]]] = None,
            text_columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'SourcePostgres':
        """
        Get an existing SourcePostgres resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The cluster to maintain this source. If not specified, the size option must be specified.
        :param pulumi.Input[str] database_name: The identifier for the source database.
        :param pulumi.Input[str] name: The identifier for the source.
        :param pulumi.Input[pulumi.InputType['SourcePostgresPostgresConnectionArgs']] postgres_connection: The PostgreSQL connection to use in the source.
        :param pulumi.Input[str] publication: The PostgreSQL publication (the replication data set containing the tables to be streamed to Materialize).
        :param pulumi.Input[str] qualified_sql_name: The fully qualified name of the source.
        :param pulumi.Input[str] schema_name: The identifier for the source schema.
        :param pulumi.Input[str] size: The size of the source.
        :param pulumi.Input[str] source_type: The type of source.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SourcePostgresTableArgs']]]] tables: Creates subsources for specific tables.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] text_columns: Decode data as text for specific columns that contain PostgreSQL types that are unsupported in Materialize.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SourcePostgresState.__new__(_SourcePostgresState)

        __props__.__dict__["cluster_name"] = cluster_name
        __props__.__dict__["database_name"] = database_name
        __props__.__dict__["name"] = name
        __props__.__dict__["postgres_connection"] = postgres_connection
        __props__.__dict__["publication"] = publication
        __props__.__dict__["qualified_sql_name"] = qualified_sql_name
        __props__.__dict__["schema_name"] = schema_name
        __props__.__dict__["size"] = size
        __props__.__dict__["source_type"] = source_type
        __props__.__dict__["tables"] = tables
        __props__.__dict__["text_columns"] = text_columns
        return SourcePostgres(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        """
        The cluster to maintain this source. If not specified, the size option must be specified.
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier for the source database.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The identifier for the source.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="postgresConnection")
    def postgres_connection(self) -> pulumi.Output['outputs.SourcePostgresPostgresConnection']:
        """
        The PostgreSQL connection to use in the source.
        """
        return pulumi.get(self, "postgres_connection")

    @property
    @pulumi.getter
    def publication(self) -> pulumi.Output[str]:
        """
        The PostgreSQL publication (the replication data set containing the tables to be streamed to Materialize).
        """
        return pulumi.get(self, "publication")

    @property
    @pulumi.getter(name="qualifiedSqlName")
    def qualified_sql_name(self) -> pulumi.Output[str]:
        """
        The fully qualified name of the source.
        """
        return pulumi.get(self, "qualified_sql_name")

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier for the source schema.
        """
        return pulumi.get(self, "schema_name")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[str]:
        """
        The size of the source.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Output[str]:
        """
        The type of source.
        """
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter
    def tables(self) -> pulumi.Output[Optional[Sequence['outputs.SourcePostgresTable']]]:
        """
        Creates subsources for specific tables.
        """
        return pulumi.get(self, "tables")

    @property
    @pulumi.getter(name="textColumns")
    def text_columns(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Decode data as text for specific columns that contain PostgreSQL types that are unsupported in Materialize.
        """
        return pulumi.get(self, "text_columns")
