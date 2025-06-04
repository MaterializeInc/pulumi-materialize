# Pulumi Provider: Materialize

[![Slack Badge](https://img.shields.io/badge/Join%20us%20on%20Slack!-blueviolet?style=flat&logo=slack&link=https://materialize.com/s/chat)](https://materialize.com/s/chat)

> **⚠️ DEPRECATED - Repository Archived**
>
> **This repository is now archived and will no longer receive updates.** 
>
> With Pulumi's new "Any Terraform Provider" framework (released August 2024), you can now use the Materialize Terraform provider directly with Pulumi without needing this separate repository. This provides instant access to the latest provider features and eliminates maintenance overhead.
>
> **Please migrate to the new approach below**
>
> For any questions or help with migration, please reach out on the [Materialize Slack](https://materialize.com/s/chat) or via email at `support@materialize.com`.

## 🚀 New Usage (Recommended)

As of **Pulumi CLI 3.130.0+**, you can use the Materialize provider directly without installing a separate package:

### Quick Start

```bash
# Create a new Pulumi project (if you haven't already)
pulumi new python  # or typescript, go, etc.

# Add the Materialize provider to your Pulumi project
pulumi package add terraform-provider MaterializeInc/materialize

# Or pin to a specific version:
# pulumi package add terraform-provider MaterializeInc/materialize 0.9.1
```

This commands automatically:
- Generates a Pulumi SDK in your project
- Download the Terraform provider
- Configures your `Pulumi.yaml`
- Provides full type safety and IntelliSense

### Usage Examples

**Python:**
```python
import pulumi_materialize as materialize

# Create a database
database = materialize.Database("my-db",
    name="pulumi-created-db"
)

# Create a cluster 
cluster = materialize.Cluster("my-cluster",
    name="pulumi-cluster",
    size="25cc"
)
```

**TypeScript:**
```typescript
import * as materialize from "./sdks/materialize";

const database = new materialize.Database("my-db", {
    name: "production-db"
});
```

**Go:**
```go
import "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
import materialize "./sdks/materialize"

database, err := materialize.NewDatabase(ctx, "my-db", &materialize.DatabaseArgs{
    Name: pulumi.String("production-db"),
})
```

### Requirements

- You will need to be using a version of Pulumi >= `3.147.0`.
- No additional setup required!

## Configuration

The configuration remains the same. Set these values using `pulumi config` or environment variables:

- `materialize:password` (environment: `MZ_PASSWORD`) - Materialize password. Required for authentication.
- `materialize:database` (environment: `MZ_DATABASE`) - Materialize database. Default is `materialize`.
- `materialize:default_region` (environment: `MZ_DEFAULT_REGION`) - The default region if not specified in the resource. Default is `aws/us-east-1`.

For self-hosted Materialize instances, you should also configure:

- `materialize:host` (environment: `MZ_HOST`) - The hostname of your Materialize instance.
- `materialize:port` (environment: `MZ_PORT`) - The port of your Materialize instance (default is 6875).

Optional configurations for testing only:

- `materialize:endpoint` (environment: `MZ_ENDPOINT`) - The endpoint for the Frontegg API.
- `materialize:cloud_endpoint` (environment: `MZ_CLOUD_ENDPOINT`) - The endpoint for the Materialize Cloud API.

**Example configuration:**
```bash
pulumi config set materialize:password "your-password" --secret
pulumi config set materialize:database "your-database"
pulumi config set materialize:default_region "aws/us-west-2"
```

## Migration Guide

### From Legacy Pulumi Package

If you were using the legacy `pulumi_materialize` package:

1. **Remove the old package:**
   ```bash
   # Python
   pip uninstall pulumi_materialize
   ```

2. **Add the new provider:**
   ```bash
   pulumi package add terraform-provider MaterializeInc/materialize
   ```

3. **Update your imports:**
   ```python
   # Old
   import pulumi_materialize as materialize

   # New (same import, but now uses generated SDK)
   import pulumi_materialize as materialize
   ```

4. **Verify your configuration** (no changes needed to config values)

### Benefits of the New Approach

- **Always up-to-date**: Automatically uses the latest Terraform provider
- **Zero maintenance**: No waiting for Pulumi package updates
- **Faster releases**: New Terraform provider features available immediately
- **Better type safety**: Generated SDKs with full IntelliSense
- **Smaller footprint**: No separate package installation required

## Advanced Usage

### Version Pinning
```bash
# Pin to a specific provider version for reproducible builds
pulumi package add terraform-provider MaterializeInc/materialize@0.9.1
```

### Local Development
```bash
# Use a local provider binary for development
pulumi package add terraform-provider ./path/to/terraform-provider-materialize
```

## Resources and Documentation

- **Materialize Terraform Provider**: [MaterializeInc/terraform-provider-materialize](https://github.com/MaterializeInc/terraform-provider-materialize)
- **Pulumi "Any Terraform Provider" Docs**: [Pulumi Registry](https://www.pulumi.com/registry/packages/terraform-provider/)
- **Materialize Documentation**: [materialize.com/docs](https://materialize.com/docs)
- **Community Support**: [Materialize Slack](https://materialize.com/s/chat)

## Need Help?

- **Provider Issues**: Report at [terraform-provider-materialize](https://github.com/MaterializeInc/terraform-provider-materialize/issues)
- **Pulumi Integration**: Check [Pulumi Community Slack](https://slack.pulumi.com/)
- **Materialize Support**: Join [Materialize Slack](https://materialize.com/s/chat)

---

**This repository is archived.** All future development happens in the [Terraform provider](https://github.com/MaterializeInc/terraform-provider-materialize). Thank you for using the Materialize Pulumi provider!
