// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Materialize.Inputs
{

    public sealed class ConnectionKafkaKafkaBrokerArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The availability zone of the Kafka broker.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// The Kafka broker, in the form of `host:port`.
        /// </summary>
        [Input("broker", required: true)]
        public Input<string> Broker { get; set; } = null!;

        /// <summary>
        /// The AWS PrivateLink connection name in Materialize.
        /// </summary>
        [Input("privatelinkConnection")]
        public Input<Inputs.ConnectionKafkaKafkaBrokerPrivatelinkConnectionArgs>? PrivatelinkConnection { get; set; }

        /// <summary>
        /// The port of the target group associated with the Kafka broker.
        /// </summary>
        [Input("targetGroupPort")]
        public Input<int>? TargetGroupPort { get; set; }

        public ConnectionKafkaKafkaBrokerArgs()
        {
        }
        public static new ConnectionKafkaKafkaBrokerArgs Empty => new ConnectionKafkaKafkaBrokerArgs();
    }
}