# Why can't I download all varieties? Should I submit multiple download queries?

The tool has a limit of N varieties, and the maximal size of the region is 50kb. If you need more, please download from AWS directly and use GATK tool.

We limited the tool, as it is taxing our cloud resources.

Please also refrain from submitting many queries at once. There is a storage limit on the AWS instance running the tool, and in case it gets exhausted, all ongoing jobs will be cancelled.