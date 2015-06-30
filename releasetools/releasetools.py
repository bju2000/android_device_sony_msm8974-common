# Copyright (C) 2014 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Custom OTA commands for Sony devices with locked bootloaders"""

def FullOTA_InstallEnd(info):
  info.script.script = [cmd for cmd in info.script.script if not "show_progress(0.100000, 0);" in cmd]
  info.script.Mount("/system")
  info.script.AppendExtra('package_extract_file("/system/bootimage/boot.img", "/dev/block/platform/msm_sdcc.1/by-name/boot");')
  info.script.AppendExtra('assert(run_program("/system/bin/propeditor.sh") == 0);')
  info.script.AppendExtra('delete("/system/bin/propeditor.sh");')
  info.script.Unmount("/system")
