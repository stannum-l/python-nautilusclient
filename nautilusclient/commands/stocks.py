# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import click
import json

from nautilusclient.api import engine
from nautilusclient.shell import pass_context
from nautilusclient import options

COMMAND_NAME = 'stocks'


@click.command(COMMAND_NAME, help="Gets stock information")
@click.argument('symbol')
@options.os_params
@pass_context
def cli(ctx, symbol, **kwargs):
    resp = engine.GoogleFinAPI().get_stocks(symbol)
    click.echo(json.dumps(resp))
