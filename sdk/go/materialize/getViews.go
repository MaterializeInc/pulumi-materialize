// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package materialize

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-materialize/sdk/go/materialize"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := materialize.GetViews(ctx, nil, nil)
//			if err != nil {
//				return err
//			}
//			_, err = materialize.GetViews(ctx, &GetViewsArgs{
//				DatabaseName: pulumi.StringRef("materialize"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			_, err = materialize.GetViews(ctx, &GetViewsArgs{
//				DatabaseName: pulumi.StringRef("materialize"),
//				SchemaName:   pulumi.StringRef("schema"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetViews(ctx *pulumi.Context, args *GetViewsArgs, opts ...pulumi.InvokeOption) (*GetViewsResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv GetViewsResult
	err := ctx.Invoke("materialize:index/getViews:GetViews", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking GetViews.
type GetViewsArgs struct {
	// Limit views to a specific database
	DatabaseName *string `pulumi:"databaseName"`
	// Limit views to a specific schema within a specific database
	SchemaName *string `pulumi:"schemaName"`
}

// A collection of values returned by GetViews.
type GetViewsResult struct {
	// Limit views to a specific database
	DatabaseName *string `pulumi:"databaseName"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Limit views to a specific schema within a specific database
	SchemaName *string `pulumi:"schemaName"`
	// The views in the account
	Views []GetViewsView `pulumi:"views"`
}

func GetViewsOutput(ctx *pulumi.Context, args GetViewsOutputArgs, opts ...pulumi.InvokeOption) GetViewsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetViewsResult, error) {
			args := v.(GetViewsArgs)
			r, err := GetViews(ctx, &args, opts...)
			var s GetViewsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetViewsResultOutput)
}

// A collection of arguments for invoking GetViews.
type GetViewsOutputArgs struct {
	// Limit views to a specific database
	DatabaseName pulumi.StringPtrInput `pulumi:"databaseName"`
	// Limit views to a specific schema within a specific database
	SchemaName pulumi.StringPtrInput `pulumi:"schemaName"`
}

func (GetViewsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetViewsArgs)(nil)).Elem()
}

// A collection of values returned by GetViews.
type GetViewsResultOutput struct{ *pulumi.OutputState }

func (GetViewsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetViewsResult)(nil)).Elem()
}

func (o GetViewsResultOutput) ToGetViewsResultOutput() GetViewsResultOutput {
	return o
}

func (o GetViewsResultOutput) ToGetViewsResultOutputWithContext(ctx context.Context) GetViewsResultOutput {
	return o
}

// Limit views to a specific database
func (o GetViewsResultOutput) DatabaseName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetViewsResult) *string { return v.DatabaseName }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetViewsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetViewsResult) string { return v.Id }).(pulumi.StringOutput)
}

// Limit views to a specific schema within a specific database
func (o GetViewsResultOutput) SchemaName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetViewsResult) *string { return v.SchemaName }).(pulumi.StringPtrOutput)
}

// The views in the account
func (o GetViewsResultOutput) Views() GetViewsViewArrayOutput {
	return o.ApplyT(func(v GetViewsResult) []GetViewsView { return v.Views }).(GetViewsViewArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetViewsResultOutput{})
}