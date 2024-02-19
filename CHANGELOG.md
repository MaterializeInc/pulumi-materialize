CHANGELOG
=========

## 0.1.5 - 2024-02-19
Update to Terraform Provider [0.6.5](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.6.5).

## 0.1.4 - 2024-02-03
Update to Terraform Provider [0.6.4](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.6.4).

## 0.1.3 - 2024-02-02
Update to Terraform Provider [0.6.3](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.6.3).

## 0.1.2 - 2024-02-01
Update to Terraform Provider [0.6.1](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.6.1).

## 0.1.1 - 2024-01-23
Update to Terraform Provider [0.6.0](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.6.0).

### Breaking Changes
* Drop `SIZE` support for sources and sinks.

## 0.1.0 - 2024-01-11
Update to Terraform Provider [0.5.0](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.5.0).

### Breaking Changes
* **Provider Configuration Changes**:
  * Deprecated the `host`, `port`, and `user` parameters in the provider configuration. These details are now derived from the app password.
  * Retained only the `password` definition in the provider configuration. This password is used to fetch all necessary connection information.
* **New `region` Configuration**:
  * Introduced a new `default_region` parameter in the provider configuration. This allows users to specify the default region for resource creation.
  * The `default_region` parameter can be overridden in specific resource configurations if a particular resource needs to be created in a non-default region.

### Migration Guide
* Before upgrading to `v0.1.0`, users should ensure that they have upgraded to `v0.0.8` which introduced a state migration necessary for `v0.1.0`. After upgrading to `v0.0.0`, users should run `pulumi refresh` to ensure that the state migration has completed successfully.

## 0.0.8 - 2023-12-14
Update to Terraform Provider [0.4.1](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.4.1).

## 0.0.7 - 2023-12-06
Update to Terraform Provider [0.3.4](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.3.4).

## 0.0.6 - 2023-11-30
Update to Terraform Provider [0.3.3](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.3.3).

## 0.0.5 - 2023-11-26
Fix issues with the Terraform Bridge in v0.0.4.

## 0.0.4 - 2023-11-23
Update to Terraform Provider [0.3.1](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.3.1).

## 0.0.3 - 2023-11-17
Update to Terraform Provider [0.3.0](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.3.0).

## 0.0.2 - 2023-10-31
Update to Terraform Provider [0.2.0](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.2.0).

## 0.0.1 - 2023-10-02
Initial release.
