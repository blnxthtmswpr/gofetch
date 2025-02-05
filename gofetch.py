# 
# Copyright (c) 2025 blnxthtmswpr
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# gofetch - simple system status fetcher
# made just for fun, feel free to include it in your os
# Thanks to stackoverflow and geeks4geeks for helping
# me with this code!



# importing the stuff that makes this work
import platform

my_system = platform.uname()


# just a fun easter egg, ascii art by ascii.co.uk
if {my_system.system} == {'Linux'}:
	print("\n")
	print("        _nnnn_        ")
	print("       dGGGGMMb")
	print("      @p~qp~~qMb")
	print("      M|@||@) M|")
	print("      @,----,JM|")
	print("     JS^|__,  qKL")
	print("\nCertified Linux System\n")

# getting system info
print(f"\nSystem: {my_system.system}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"PC Name: {my_system.node}")
print(f"Processor: {my_system.processor}\n\n")
