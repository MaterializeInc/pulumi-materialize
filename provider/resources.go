// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package materialize

import (
	"fmt"
	"path/filepath"

	"github.com/MaterializeInc/pulumi-materialize/provider/pkg/version"

	materialize "github.com/MaterializeInc/terraform-provider-materialize/pkg/provider"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "materialize"
	// modules:
	mainMod = "index" // the materialize module
)

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c shim.ResourceConfig) error {
	return nil
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := shimv2.NewProvider(materialize.Provider(fmt.Sprintf("%s-pulumi-materialize", version.Version)))

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:                    p,
		Name:                 "materialize",
		Description:          "A Pulumi package for creating and managing materialize cloud resources.",
		Keywords:             []string{"pulumi", "materialize", "category/cloud"},
		License:              "Apache-2.0",
		Publisher:            "Materialize Inc",
		LogoURL:              "https://github.com/MaterializeInc/pulumi-materialize/assets/7467658/77df931a-b571-461f-a279-dac62fbbc236",
		GitHubOrg:            "MaterializeInc",
		Homepage:             "https://github.com/MaterializeInc/terraform-provider-materialize",
		Repository:           "https://github.com/MaterializeInc/terraform-provider-materialize",
		PluginDownloadURL:    "github://api.github.com/MaterializeInc/pulumi-materialize",
		DisplayName:          "Materialize",
		PreConfigureCallback: preConfigureCallback,
		Config: map[string]*tfbridge.SchemaInfo{
			"password": {
				Default: &tfbridge.DefaultInfo{EnvVars: []string{"MZ_PASSWORD"}},
			},
			"database": {
				Default: &tfbridge.DefaultInfo{EnvVars: []string{"MZ_DATABASE"}},
			},
			"endpoint": {
				Default: &tfbridge.DefaultInfo{EnvVars: []string{"MZ_ENDPOINT"}},
			},
			"cloud_endpoint": {
				Default: &tfbridge.DefaultInfo{EnvVars: []string{"MZ_CLOUD_ENDPOINT"}},
			},
			"base_endpoint": {
				Default: &tfbridge.DefaultInfo{EnvVars: []string{"MZ_BASE_ENDPOINT"}},
			},
			"default_region": {
				Default: &tfbridge.DefaultInfo{EnvVars: []string{"MZ_DEFAULT_REGION"}},
			},
			"sslmode": {
				Default: &tfbridge.DefaultInfo{EnvVars: []string{"MZ_SSLMODE"}},
			},
		},
		Resources: map[string]*tfbridge.ResourceInfo{
			"materialize_app_password":                         {Tok: tfbridge.MakeResource(mainPkg, mainMod, "AppPassword")},
			"materialize_cluster":                              {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Cluster")},
			"materialize_cluster_grant":                        {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantCluster")},
			"materialize_cluster_grant_default_privilege":      {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantClusterDefaultPrivilege")},
			"materialize_cluster_replica":                      {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ClusterReplica")},
			"materialize_connection_aws":                       {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ConnectionAws")},
			"materialize_connection_aws_privatelink":           {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ConnectionAwsPrivatelink")},
			"materialize_connection_confluent_schema_registry": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ConnectionConfluentSchemaRegistry")},
			"materialize_connection_kafka":                     {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ConnectionKafka")},
			"materialize_connection_mysql":                     {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ConnectionMysql")},
			"materialize_connection_postgres":                  {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ConnectionPostgres")},
			"materialize_connection_ssh_tunnel":                {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ConnectionSshTunnel")},
			"materialize_connection_grant":                     {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantConnection")},
			"materialize_connection_grant_default_privilege":   {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantConnectionDefaultPrivilege")},
			"materialize_database":                             {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Database")},
			"materialize_database_grant":                       {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantDatabase")},
			"materialize_database_grant_default_privilege":     {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantDatabaseDefaultPrivilege")},
			"materialize_grant_system_privilege":               {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantSystemPrivilege")},
			"materialize_index":                                {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Index")},
			"materialize_materialized_view":                    {Tok: tfbridge.MakeResource(mainPkg, mainMod, "MaterializedView")},
			"materialize_materialized_view_grant":              {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantMaterializedView")},
			"materialize_role":                                 {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Role")},
			"materialize_role_grant":                           {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantRole")},
			"materialize_schema":                               {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Schema")},
			"materialize_schema_grant":                         {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantSchema")},
			"materialize_schema_grant_default_privilege":       {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantSchemaDefaultPrivilege")},
			"materialize_scim_config":                          {Tok: tfbridge.MakeResource(mainPkg, mainMod, "SCIM2Configuration")},
			"materialize_secret":                               {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Secret")},
			"materialize_secret_grant":                         {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantSecret")},
			"materialize_secret_grant_default_privilege":       {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantSecretDefaultPrivilege")},
			"materialize_sink_kafka":                           {Tok: tfbridge.MakeResource(mainPkg, mainMod, "SinkKafka")},
			"materialize_source_kafka":                         {Tok: tfbridge.MakeResource(mainPkg, mainMod, "SourceKafka")},
			"materialize_source_load_generator":                {Tok: tfbridge.MakeResource(mainPkg, mainMod, "SourceLoadgen")},
			"materialize_source_mysql":                         {Tok: tfbridge.MakeResource(mainPkg, mainMod, "SourceMysql")},
			"materialize_source_postgres":                      {Tok: tfbridge.MakeResource(mainPkg, mainMod, "SourcePostgres")},
			"materialize_source_webhook":                       {Tok: tfbridge.MakeResource(mainPkg, mainMod, "SourceWebhook")},
			"materialize_source_grant":                         {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantSource")},
			"materialize_sso_config":                           {Tok: tfbridge.MakeResource(mainPkg, mainMod, "SSOConfig")},
			"materialize_sso_domain":                           {Tok: tfbridge.MakeResource(mainPkg, mainMod, "SSODomain")},
			"materialize_sso_group_mapping":                    {Tok: tfbridge.MakeResource(mainPkg, mainMod, "SSORoleGroupMapping")},
			"materialize_sso_default_roles":                    {Tok: tfbridge.MakeResource(mainPkg, mainMod, "SSODefaultRoles")},
			"materialize_system_parameter":                     {Tok: tfbridge.MakeResource(mainPkg, mainMod, "SystemParameter")},
			"materialize_table":                                {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Table")},
			"materialize_table_grant":                          {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantTable")},
			"materialize_table_grant_default_privilege":        {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantTableDefaultPrivilege")},
			"materialize_type":                                 {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Type")},
			"materialize_type_grant":                           {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantType")},
			"materialize_type_grant_default_privilege":         {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantTypeDefaultPrivilege")},
			"materialize_view":                                 {Tok: tfbridge.MakeResource(mainPkg, mainMod, "View")},
			"materialize_view_grant":                           {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GrantView")},
			"materialize_user":                                 {Tok: tfbridge.MakeResource(mainPkg, mainMod, "User")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"materialize_cluster":           {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetClusters")},
			"materialize_cluster_replica":   {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetClusterReplicas")},
			"materialize_connection":        {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetConnections")},
			"materialize_current_database":  {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetCurrentDatabase")},
			"materialize_current_cluster":   {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetCurrentCluster")},
			"materialize_database":          {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetDatabases")},
			"materialize_egress_ips":        {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetEgressIps")},
			"materialize_index":             {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetIndexes")},
			"materialize_materialized_view": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetMaterializedViews")},
			"materialize_region":            {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "Region")},
			"materialize_role":              {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetRoles")},
			"materialize_schema":            {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetSchemas")},
			"materialize_secret":            {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetSecrets")},
			"materialize_sink":              {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetSinks")},
			"materialize_source":            {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetSources")},
			"materialize_scim_groups":       {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetSCIMGroups")},
			"materialize_scim_configs":      {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetSCIMConfigs")},
			"materialize_sso_config":        {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetSSOConfig")},
			"materialize_system_parameter":  {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetSystemParameters")},
			"materialize_table":             {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetTables")},
			"materialize_type":              {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetTypes")},
			"materialize_view":              {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetViews")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			// See the documentation for tfbridge.OverlayInfo for how to lay out this
			// section, or refer to the AWS provider. Delete this section if there are
			// no overlay files.
			//Overlay: &tfbridge.OverlayInfo{},
		},
		Python: &tfbridge.PythonInfo{
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/pulumi/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}
