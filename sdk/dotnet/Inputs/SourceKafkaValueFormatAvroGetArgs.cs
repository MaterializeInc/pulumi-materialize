// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Materialize.Inputs
{

    public sealed class SourceKafkaValueFormatAvroGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("keyStrategy")]
        public Input<string>? KeyStrategy { get; set; }

        [Input("schemaRegistryConnection", required: true)]
        public Input<Inputs.SourceKafkaValueFormatAvroSchemaRegistryConnectionGetArgs> SchemaRegistryConnection { get; set; } = null!;

        [Input("valueStrategy")]
        public Input<string>? ValueStrategy { get; set; }

        public SourceKafkaValueFormatAvroGetArgs()
        {
        }
        public static new SourceKafkaValueFormatAvroGetArgs Empty => new SourceKafkaValueFormatAvroGetArgs();
    }
}