
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


"""Creates a Container VM with the provided Container manifest."""

from container_helper import GenerateManifest


COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GlobalComputeUrl(project, collection, name):
  return ''.join([COMPUTE_URL_BASE, 'projects/', project,
                  '/global/', collection, '/', name])


def ZonalComputeUrl(project, zone, collection, name):
  return ''.join([COMPUTE_URL_BASE, 'projects/', project,
                  '/zones/', zone, '/', collection, '/', name])


def GenerateConfig(context):
  """Generate configuration."""

  base_name = context.env['name']

  # Properties for the container-based instance.
  instance = {
      'zone': context.properties['zone'],
      'machineType': ZonalComputeUrl(context.env['project'],
                                     context.properties['zone'],
                                     'machineTypes',
                                     'f1-micro'),
      'metadata': {
          'items': [{
              'key': 'gce-container-declaration',
              'value': GenerateManifest(context)
              }]
          },
      'disks': [{
          'deviceName': 'boot',
          'type': 'PERSISTENT',
          'autoDelete': True,
          'boot': True,
          'initializeParams': {
              'diskName': base_name + '-disk',
              'sourceImage': GlobalComputeUrl('cos-cloud',
                                              'images',
                                              context.properties[
                                                  'containerImage'])
              },
          }],
      'networkInterfaces': [{
          'accessConfigs': [{
              'name': 'external-nat',
              'type': 'ONE_TO_ONE_NAT'
              }],
          'network': GlobalComputeUrl(context.env['project'],
                                      'networks',
                                      'default')
          }],
        'serviceAccounts': [{
            'email': 'default',
            'scopes': ['https://www.googleapis.com/auth/logging.write']
            }]
      }

  # Resources to return.
  resources = {
      'resources': [{
          'name': base_name,
          'type': 'compute.v1.instance',
          'properties': instance
          }]
      }

  return resources