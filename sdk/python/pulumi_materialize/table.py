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

__all__ = ['TableArgs', 'Table']

@pulumi.input_type
class TableArgs:
    def __init__(__self__, *,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Table resource.
        :param pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]] columns: Column of the table.
        :param pulumi.Input[str] database_name: The identifier for the table database.
        :param pulumi.Input[str] name: The identifier for the table.
        :param pulumi.Input[str] schema_name: The identifier for the table schema.
        """
        if columns is not None:
            pulumi.set(__self__, "columns", columns)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if schema_name is not None:
            pulumi.set(__self__, "schema_name", schema_name)

    @property
    @pulumi.getter
    def columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]]:
        """
        Column of the table.
        """
        return pulumi.get(self, "columns")

    @columns.setter
    def columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]]):
        pulumi.set(self, "columns", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the table database.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the table.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the table schema.
        """
        return pulumi.get(self, "schema_name")

    @schema_name.setter
    def schema_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_name", value)


@pulumi.input_type
class _TableState:
    def __init__(__self__, *,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 qualified_sql_name: Optional[pulumi.Input[str]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Table resources.
        :param pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]] columns: Column of the table.
        :param pulumi.Input[str] database_name: The identifier for the table database.
        :param pulumi.Input[str] name: The identifier for the table.
        :param pulumi.Input[str] qualified_sql_name: The fully qualified name of the table.
        :param pulumi.Input[str] schema_name: The identifier for the table schema.
        """
        if columns is not None:
            pulumi.set(__self__, "columns", columns)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if qualified_sql_name is not None:
            pulumi.set(__self__, "qualified_sql_name", qualified_sql_name)
        if schema_name is not None:
            pulumi.set(__self__, "schema_name", schema_name)

    @property
    @pulumi.getter
    def columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]]:
        """
        Column of the table.
        """
        return pulumi.get(self, "columns")

    @columns.setter
    def columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]]):
        pulumi.set(self, "columns", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the table database.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the table.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="qualifiedSqlName")
    def qualified_sql_name(self) -> Optional[pulumi.Input[str]]:
        """
        The fully qualified name of the table.
        """
        return pulumi.get(self, "qualified_sql_name")

    @qualified_sql_name.setter
    def qualified_sql_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "qualified_sql_name", value)

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the table schema.
        """
        return pulumi.get(self, "schema_name")

    @schema_name.setter
    def schema_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_name", value)


class Table(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableColumnArgs']]]]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A table persists in durable storage and can be written to, updated and seamlessly joined with other tables, views or sources.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_materialize as materialize

        simple_table = materialize.Table("simpleTable",
            schema_name=materialize_schema["schema"]["name"],
            database_name=materialize_database["database"]["name"],
            columns=[
                materialize.TableColumnArgs(
                    name="column_1",
                    type="text",
                ),
                materialize.TableColumnArgs(
                    name="column_2",
                    type="int",
                ),
                materialize.TableColumnArgs(
                    name="column_3",
                    type="text",
                    nullable=True,
                ),
            ])
        ```

        ## Import

        # Views can be imported using the table id

        ```sh
         $ pulumi import materialize:index/table:Table example_table <table_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableColumnArgs']]]] columns: Column of the table.
        :param pulumi.Input[str] database_name: The identifier for the table database.
        :param pulumi.Input[str] name: The identifier for the table.
        :param pulumi.Input[str] schema_name: The identifier for the table schema.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TableArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A table persists in durable storage and can be written to, updated and seamlessly joined with other tables, views or sources.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_materialize as materialize

        simple_table = materialize.Table("simpleTable",
            schema_name=materialize_schema["schema"]["name"],
            database_name=materialize_database["database"]["name"],
            columns=[
                materialize.TableColumnArgs(
                    name="column_1",
                    type="text",
                ),
                materialize.TableColumnArgs(
                    name="column_2",
                    type="int",
                ),
                materialize.TableColumnArgs(
                    name="column_3",
                    type="text",
                    nullable=True,
                ),
            ])
        ```

        ## Import

        # Views can be imported using the table id

        ```sh
         $ pulumi import materialize:index/table:Table example_table <table_id>
        ```

        :param str resource_name: The name of the resource.
        :param TableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableColumnArgs']]]]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TableArgs.__new__(TableArgs)

            __props__.__dict__["columns"] = columns
            __props__.__dict__["database_name"] = database_name
            __props__.__dict__["name"] = name
            __props__.__dict__["schema_name"] = schema_name
            __props__.__dict__["qualified_sql_name"] = None
        super(Table, __self__).__init__(
            'materialize:index/table:Table',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableColumnArgs']]]]] = None,
            database_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            qualified_sql_name: Optional[pulumi.Input[str]] = None,
            schema_name: Optional[pulumi.Input[str]] = None) -> 'Table':
        """
        Get an existing Table resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableColumnArgs']]]] columns: Column of the table.
        :param pulumi.Input[str] database_name: The identifier for the table database.
        :param pulumi.Input[str] name: The identifier for the table.
        :param pulumi.Input[str] qualified_sql_name: The fully qualified name of the table.
        :param pulumi.Input[str] schema_name: The identifier for the table schema.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TableState.__new__(_TableState)

        __props__.__dict__["columns"] = columns
        __props__.__dict__["database_name"] = database_name
        __props__.__dict__["name"] = name
        __props__.__dict__["qualified_sql_name"] = qualified_sql_name
        __props__.__dict__["schema_name"] = schema_name
        return Table(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def columns(self) -> pulumi.Output[Optional[Sequence['outputs.TableColumn']]]:
        """
        Column of the table.
        """
        return pulumi.get(self, "columns")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier for the table database.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The identifier for the table.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="qualifiedSqlName")
    def qualified_sql_name(self) -> pulumi.Output[str]:
        """
        The fully qualified name of the table.
        """
        return pulumi.get(self, "qualified_sql_name")

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier for the table schema.
        """
        return pulumi.get(self, "schema_name")
