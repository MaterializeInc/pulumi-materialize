// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Materialize.Outputs
{

    [OutputType]
    public sealed class GetClusterReplicasClusterReplicaResult
    {
        public readonly string AvailabilityZone;
        public readonly string Cluster;
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        public readonly string Size;

        [OutputConstructor]
        private GetClusterReplicasClusterReplicaResult(
            string availabilityZone,

            string cluster,

            string id,

            string name,

            string size)
        {
            AvailabilityZone = availabilityZone;
            Cluster = cluster;
            Id = id;
            Name = name;
            Size = size;
        }
    }
}