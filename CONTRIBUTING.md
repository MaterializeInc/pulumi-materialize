# Contributing

> **⚠️ Repository Archived**
>
> **This repository is archived and no longer accepts contributions.**
>
> With Pulumi's new "Any Terraform Provider" framework, this separate provider repository is no longer needed. Users can now access the Materialize provider directly through the Terraform provider.

## Where to Contribute Now

### Terraform Provider (Main Development)

All provider development now happens in the **Terraform provider repository**:

- **Repository**: [MaterializeInc/terraform-provider-materialize](https://github.com/MaterializeInc/terraform-provider-materialize)
- **Issues**: [Report bugs and feature requests here](https://github.com/MaterializeInc/terraform-provider-materialize/issues)
- **Pull Requests**: [Submit provider improvements here](https://github.com/MaterializeInc/terraform-provider-materialize/pulls)

### Pulumi Integration Issues

For issues specific to the Pulumi integration or "Any Terraform Provider" framework:

- **Pulumi Issues**: [pulumi/pulumi](https://github.com/pulumi/pulumi/issues)
- **Pulumi 'Any Terraform Provider' Issues**: [pulumi/pulumi-terraform-provider](https://github.com/pulumi/pulumi-terraform-provider/issues)
- **Community Support**: [Pulumi Community Slack](https://slack.pulumi.com/)

## How the New System Works

The new Pulumi "Any Terraform Provider" framework automatically:

1. **Downloads the Terraform provider** from the HashiCorp registry
2. **Generates Pulumi SDKs** locally in your project
3. **Provides the same developer experience** as traditional Pulumi providers
4. **Stays automatically up-to-date** with Terraform provider releases

This eliminates the need for:
- Separate Pulumi provider repositories
- Manual SDK generation and publishing
- Version synchronization between Terraform and Pulumi providers
- Maintenance overhead for multiple language SDKs

## Migration for Contributors

If you were a contributor to this repository:

### For Provider Features and Bug Fixes
**Contribute to the Terraform provider instead:**
- All provider logic, resources, and data sources are defined there
- Changes automatically become available to Pulumi users as new versions are released

## Historical Context

This repository previously:
1. **Bridged** the Terraform provider to Pulumi using the Pulumi Terraform Bridge
2. **Generated and published** Only the Python SDK
3. **Managed releases** and version synchronization

The new approach provides all these benefits automatically without requiring separate repositories or maintenance.

---

**For all future contributions, please visit**: [MaterializeInc/terraform-provider-materialize](https://github.com/MaterializeInc/terraform-provider-materialize)
