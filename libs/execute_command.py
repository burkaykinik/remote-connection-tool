from distutils import command
import sys
import subprocess


def execute_command(command_list):
    process = subprocess.Popen(command_list,stdout=subprocess.PIPE, stderr= subprocess.PIPE)
    stdout, stderr = process.communicate()

    return stdout,stderr