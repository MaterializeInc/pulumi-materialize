# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['MaterializedViewArgs', 'MaterializedView']

@pulumi.input_type
class MaterializedViewArgs:
    def __init__(__self__, *,
                 statement: pulumi.Input[str],
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MaterializedView resource.
        :param pulumi.Input[str] statement: The SQL statement to create the materialized view.
        :param pulumi.Input[str] cluster_name: The cluster to maintain the materialized view. If not specified, defaults to the default cluster.
        :param pulumi.Input[str] database_name: The identifier for the materialized view database.
        :param pulumi.Input[str] name: The identifier for the materialized view.
        :param pulumi.Input[str] schema_name: The identifier for the materialized view schema.
        """
        pulumi.set(__self__, "statement", statement)
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if schema_name is not None:
            pulumi.set(__self__, "schema_name", schema_name)

    @property
    @pulumi.getter
    def statement(self) -> pulumi.Input[str]:
        """
        The SQL statement to create the materialized view.
        """
        return pulumi.get(self, "statement")

    @statement.setter
    def statement(self, value: pulumi.Input[str]):
        pulumi.set(self, "statement", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        The cluster to maintain the materialized view. If not specified, defaults to the default cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the materialized view database.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the materialized view.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the materialized view schema.
        """
        return pulumi.get(self, "schema_name")

    @schema_name.setter
    def schema_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_name", value)


@pulumi.input_type
class _MaterializedViewState:
    def __init__(__self__, *,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 qualified_sql_name: Optional[pulumi.Input[str]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None,
                 statement: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MaterializedView resources.
        :param pulumi.Input[str] cluster_name: The cluster to maintain the materialized view. If not specified, defaults to the default cluster.
        :param pulumi.Input[str] database_name: The identifier for the materialized view database.
        :param pulumi.Input[str] name: The identifier for the materialized view.
        :param pulumi.Input[str] qualified_sql_name: The fully qualified name of the materialized view.
        :param pulumi.Input[str] schema_name: The identifier for the materialized view schema.
        :param pulumi.Input[str] statement: The SQL statement to create the materialized view.
        """
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if qualified_sql_name is not None:
            pulumi.set(__self__, "qualified_sql_name", qualified_sql_name)
        if schema_name is not None:
            pulumi.set(__self__, "schema_name", schema_name)
        if statement is not None:
            pulumi.set(__self__, "statement", statement)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        The cluster to maintain the materialized view. If not specified, defaults to the default cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the materialized view database.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the materialized view.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="qualifiedSqlName")
    def qualified_sql_name(self) -> Optional[pulumi.Input[str]]:
        """
        The fully qualified name of the materialized view.
        """
        return pulumi.get(self, "qualified_sql_name")

    @qualified_sql_name.setter
    def qualified_sql_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "qualified_sql_name", value)

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the materialized view schema.
        """
        return pulumi.get(self, "schema_name")

    @schema_name.setter
    def schema_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_name", value)

    @property
    @pulumi.getter
    def statement(self) -> Optional[pulumi.Input[str]]:
        """
        The SQL statement to create the materialized view.
        """
        return pulumi.get(self, "statement")

    @statement.setter
    def statement(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "statement", value)


class MaterializedView(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None,
                 statement: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A materialized view persists in durable storage and can be written to, updated and seamlessly joined with other views, views or sources.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_materialize as materialize

        simple_materialized_view_materialized_view = materialize.MaterializedView("simpleMaterializedViewMaterializedView",
            schema_name=materialize_schema["schema"]["name"],
            database_name=materialize_database["database"]["name"],
            statement=f\"\"\"SELECT
            *
        FROM
            {materialize_table["simple_table"]["qualified_name"]}
        \"\"\",
            opts=pulumi.ResourceOptions(depends_on=[materialize_table["simple_table"]]))
        simple_materialized_view_index_materialized_view_materialized_view = materialize.MaterializedView("simpleMaterializedViewIndex/materializedViewMaterializedView",
            schema_name=materialize_schema["schema"]["name"],
            database_name=materialize_database["database"]["name"],
            statement="SELECT * FROM materialize.public.simple_table")
        ```

        ## Import

        # Materialized views can be imported using the source id

        ```sh
         $ pulumi import materialize:index/materializedView:MaterializedView example_materialize_view <view_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The cluster to maintain the materialized view. If not specified, defaults to the default cluster.
        :param pulumi.Input[str] database_name: The identifier for the materialized view database.
        :param pulumi.Input[str] name: The identifier for the materialized view.
        :param pulumi.Input[str] schema_name: The identifier for the materialized view schema.
        :param pulumi.Input[str] statement: The SQL statement to create the materialized view.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MaterializedViewArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A materialized view persists in durable storage and can be written to, updated and seamlessly joined with other views, views or sources.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_materialize as materialize

        simple_materialized_view_materialized_view = materialize.MaterializedView("simpleMaterializedViewMaterializedView",
            schema_name=materialize_schema["schema"]["name"],
            database_name=materialize_database["database"]["name"],
            statement=f\"\"\"SELECT
            *
        FROM
            {materialize_table["simple_table"]["qualified_name"]}
        \"\"\",
            opts=pulumi.ResourceOptions(depends_on=[materialize_table["simple_table"]]))
        simple_materialized_view_index_materialized_view_materialized_view = materialize.MaterializedView("simpleMaterializedViewIndex/materializedViewMaterializedView",
            schema_name=materialize_schema["schema"]["name"],
            database_name=materialize_database["database"]["name"],
            statement="SELECT * FROM materialize.public.simple_table")
        ```

        ## Import

        # Materialized views can be imported using the source id

        ```sh
         $ pulumi import materialize:index/materializedView:MaterializedView example_materialize_view <view_id>
        ```

        :param str resource_name: The name of the resource.
        :param MaterializedViewArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MaterializedViewArgs, pulumi.ResourceOptions, *args, **kwargs)
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
                 schema_name: Optional[pulumi.Input[str]] = None,
                 statement: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MaterializedViewArgs.__new__(MaterializedViewArgs)

            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["database_name"] = database_name
            __props__.__dict__["name"] = name
            __props__.__dict__["schema_name"] = schema_name
            if statement is None and not opts.urn:
                raise TypeError("Missing required property 'statement'")
            __props__.__dict__["statement"] = statement
            __props__.__dict__["qualified_sql_name"] = None
        super(MaterializedView, __self__).__init__(
            'materialize:index/materializedView:MaterializedView',
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
            qualified_sql_name: Optional[pulumi.Input[str]] = None,
            schema_name: Optional[pulumi.Input[str]] = None,
            statement: Optional[pulumi.Input[str]] = None) -> 'MaterializedView':
        """
        Get an existing MaterializedView resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The cluster to maintain the materialized view. If not specified, defaults to the default cluster.
        :param pulumi.Input[str] database_name: The identifier for the materialized view database.
        :param pulumi.Input[str] name: The identifier for the materialized view.
        :param pulumi.Input[str] qualified_sql_name: The fully qualified name of the materialized view.
        :param pulumi.Input[str] schema_name: The identifier for the materialized view schema.
        :param pulumi.Input[str] statement: The SQL statement to create the materialized view.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MaterializedViewState.__new__(_MaterializedViewState)

        __props__.__dict__["cluster_name"] = cluster_name
        __props__.__dict__["database_name"] = database_name
        __props__.__dict__["name"] = name
        __props__.__dict__["qualified_sql_name"] = qualified_sql_name
        __props__.__dict__["schema_name"] = schema_name
        __props__.__dict__["statement"] = statement
        return MaterializedView(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[Optional[str]]:
        """
        The cluster to maintain the materialized view. If not specified, defaults to the default cluster.
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier for the materialized view database.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The identifier for the materialized view.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="qualifiedSqlName")
    def qualified_sql_name(self) -> pulumi.Output[str]:
        """
        The fully qualified name of the materialized view.
        """
        return pulumi.get(self, "qualified_sql_name")

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier for the materialized view schema.
        """
        return pulumi.get(self, "schema_name")

    @property
    @pulumi.getter
    def statement(self) -> pulumi.Output[str]:
        """
        The SQL statement to create the materialized view.
        """
        return pulumi.get(self, "statement")
