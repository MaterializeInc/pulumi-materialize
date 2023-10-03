---
title: Materialize
meta_desc: Provides an overview of the Materialize provider for Pulumi.
layout: package
---

[![Slack Badge](https://img.shields.io/badge/Join%20us%20on%20Slack!-blueviolet?style=flat&logo=slack&link=https://materialize.com/s/chat)](https://materialize.com/s/chat)

A [Pulumi](https://pulumi.com) provider for managing resources in a [Materialize](https://materialize.com/) account.

## Example

{{< chooser language "python" >}}
{{% choosable language python %}}

```python
import pulumi_materialize

pulumi_materialize.Cluster(
    resource_name="example",
    name="pulumi-cluster",
    size="3xsmall",
)
```

{{% /choosable %}}
{{< /chooser >}}