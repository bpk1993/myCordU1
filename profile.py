"""One bare-metal x86 node running Ubuntu 14.04.5 (updated to latest packages as of 2017-02-10)

Instructions:
Log in and poke around; you have complete root access using `sudo`"""

#
# NOTE: This code was machine converted. An actual human would not
#       write code like this!
#

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab
import geni.rspec.igext as IG

# Create a portal object,
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Node node
node = request.RawPC('node')
node.disk_image = 'urn:publicid:IDN+utah.cloudlab.us+image+xos-PG0:OnePC-Ubuntu14.04.5:0'

# Install and execute scripts on the node
node.addService(pg.Install(url="https://github.com/zdw/geni-groupadd/archive/master.tar.gz", path="/local"))
node.addService(pg.Execute(shell="bash", command="/local/geni-groupadd-master/add_docker_libvirtd_groups.sh"))

apool = IG.AddressPool("nm",2)
request.addResource(apool)

# Install and execute a script that is contained in the repository.
node.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))

# Print the generated rspec
pc.printRequestRSpec(request)
