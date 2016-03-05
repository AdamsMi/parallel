#!/usr/bin/env python
from mpi4py import MPI
import socket

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()


def master(isMpiSend = True):
	start = MPI.Wtime()
	comm.send("1", dest = 1)
	comm.recv(source = 1)
	end = MPI.Wtime()
	latency = 1000 * (end - start)/2
	print "latency: ", latency

def slave(isMpiSend = True):
	comm.recv(source = 0)
	comm.send("0", dest = 0)


if size == 2:
	if rank == 0:
		master()
	else:
		slave()

else:
	print "wrong size of world: ", size

