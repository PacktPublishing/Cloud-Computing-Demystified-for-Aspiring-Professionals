
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


"""Helper methods for working with containers in config."""

import six
import yaml


def GenerateManifest(context):
  """Generates a Container Manifest given a Template context.

  Args:
    context: Template context, which must contain dockerImage and port
        properties, and an optional dockerEnv property.

  Returns:
    A Container Manifest as a YAML string.
  """
  env_list = []
  if 'dockerEnv' in context.properties:
    for key, value in six.iteritems(context.properties['dockerEnv']):
      env_list.append({'name': key, 'value': str(value)})

  manifest = {
      'apiVersion': 'v1',
      'kind': 'Pod',
      'metadata': {
          'name': str(context.env['name'])
          },
      'spec': {
          'containers': [{
              'name': str(context.env['name']),
              'image': context.properties['dockerImage'],
              'ports': [{
                  'hostPort': context.properties['port'],
                  'containerPort': context.properties['port']
                  }],
              }]
          }
      }

  if env_list:
    manifest['spec']['containers'][0]['env'] = env_list

  return yaml.dump(manifest, default_flow_style=False)