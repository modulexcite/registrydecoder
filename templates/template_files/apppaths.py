#
# Registry Decoder
# Copyright (c) 2011 Digital Forensics Solutions, LLC
#
# Contact email:  registrydecoder@digitalforensicssolutions.com
#
# Authors:
# Andrew Case       - andrew@digitalforensicssolutions.com
# Lodovico Marziale - vico@digitalforensicssolutions.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details. 
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA 
#
# Application Paths

pluginname = "Application Paths"
description = "Displays the exe files for each application listed in the Software\AppPaths"
hive = "SOFTWARE"    
documentation = ""

import sys

def run_me():
    
    reg_set_report_header(("Executable", "Path"))
    regkey = reg_get_required_key("\Microsoft\Windows\CurrentVersion\App Paths")
    
    subkeys = reg_get_subkeys(regkey)
    for key in subkeys:
        if reg_get_key_name(key).endswith(".exe"):
            path = ""
            for val in reg_get_values(key):
                
                if reg_get_value_name(val) == "NONE":
                    path = reg_get_value_data(val)
            reg_report((reg_get_key_name(key), path)) 





