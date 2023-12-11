"""A Python Pulumi program"""

import pulumi
import pulumi_materialize as materialize

database = materialize.Database("pulumi-database")

pulumi.export("database", database.name)