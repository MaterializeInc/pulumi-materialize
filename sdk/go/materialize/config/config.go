// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

// The Materialize database
func GetDatabase(ctx *pulumi.Context) string {
	return config.Get(ctx, "materialize:database")
}

// Materialize host
func GetHost(ctx *pulumi.Context) string {
	return config.Get(ctx, "materialize:host")
}

// Materialize host
func GetPassword(ctx *pulumi.Context) string {
	return config.Get(ctx, "materialize:password")
}

// The Materialize port number to connect to at the server host
func GetPort(ctx *pulumi.Context) int {
	return config.GetInt(ctx, "materialize:port")
}

// Enable to test the provider locally
func GetTesting(ctx *pulumi.Context) bool {
	return config.GetBool(ctx, "materialize:testing")
}

// Materialize username
func GetUsername(ctx *pulumi.Context) string {
	return config.Get(ctx, "materialize:username")
}