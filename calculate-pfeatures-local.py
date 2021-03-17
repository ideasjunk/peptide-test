import pandas as pd

from Pfeature.pfeature import aac_wp
from Pfeature.pfeature import dpc_wp
from Pfeature.pfeature import tpc_wp
from Pfeature.pfeature import atc_wp
from Pfeature.pfeature import btc_wp
from Pfeature.pfeature import pcp_wp
from Pfeature.pfeature import aai_wp
from Pfeature.pfeature import rri_wp
from Pfeature.pfeature import ddr_wp
from Pfeature.pfeature import pri_wp
from Pfeature.pfeature import sep_wp
from Pfeature.pfeature import ser_wp
from Pfeature.pfeature import spc_wp
from Pfeature.pfeature import acr_wp
from Pfeature.pfeature import ctc_wp
from Pfeature.pfeature import ctd_wp
from Pfeature.pfeature import paac_wp
from Pfeature.pfeature import apaac_wp
from Pfeature.pfeature import qos_wp
from Pfeature.pfeature import soc_wp

def aac(input):
	a = input.rstrip('txt')
	output=a+'aac.csv'
	df_out=aac_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

aac('train_po_cdhit.txt')

aac('train_ne_cdhit.txt')


def dpc(input):
  a = input.rstrip('txt')
  output = a + 'dpc.csv'
  df_out = dpc_wp(input, output, 1)
  df_in = pd.read_csv(output)
  return df_in

feature=dpc('train_po_cdhit.txt')
feature

feature=dpc('train_ne_cdhit.txt')
feature


def tpc(input):
	a = input.rstrip('txt')
	output=a+'tpc.csv'
	df_out=tpc_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=tpc('train_po_cdhit.txt')
feature

feature=tpc('train_ne_cdhit.txt')
feature


def atc(input):
	a = input.rstrip('txt')
	output=a+'atc.csv'
	df_out=atc_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=atc('train_po_cdhit.txt')
feature

feature=atc('train_ne_cdhit.txt')
feature


def btc(input):
	a = input.rstrip('txt')
	output=a+'btc.csv'
	df_out=btc_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=btc('train_po_cdhit.txt')
feature

feature=btc('train_ne_cdhit.txt')
feature


def pcp(input):
	a = input.rstrip('txt')
	output=a+'pcp.csv'
	df_out=pcp_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=pcp('train_po_cdhit.txt')
feature

feature=pcp('train_ne_cdhit.txt')
feature


def aai(input):
	a = input.rstrip('txt')
	output=a+'aai.csv'
	df_out=aai_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=aai('train_po_cdhit.txt')
feature

feature=aai('train_ne_cdhit.txt')
feature


def rri(input):
	a = input.rstrip('txt')
	output=a+'rri.csv'
	df_out=rri_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=rri('train_po_cdhit.txt')
feature

feature=rri('train_ne_cdhit.txt')
feature


def ddr(input):
	a = input.rstrip('txt')
	output=a+'ddr.csv'
	df_out=ddr_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=ddr('train_po_cdhit.txt')
feature

feature=ddr('train_ne_cdhit.txt')
feature


def pri(input):
	a = input.rstrip('txt')
	output=a+'pri.csv'
	df_out=pri_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=pri('train_po_cdhit.txt')
feature

feature=pri('train_ne_cdhit.txt')
feature


def sep(input):
	a = input.rstrip('txt')
	output=a+'sep.csv'
	df_out=sep_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=sep('train_po_cdhit.txt')
feature

feature=sep('train_ne_cdhit.txt')
feature


def ser(input):
	a = input.rstrip('txt')
	output=a+'ser.csv'
	df_out=ser_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=ser('train_po_cdhit.txt')
feature

feature=ser('train_ne_cdhit.txt')
feature


def spc(input):
	a = input.rstrip('txt')
	output=a+'spc.csv'
	df_out=spc_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=spc('train_po_cdhit.txt')
feature

feature=spc('train_ne_cdhit.txt')
feature


def acr(input):
	a = input.rstrip('txt')
	output=a+'acr.csv'
	df_out=acr_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=acr('train_po_cdhit.txt')
feature

feature=acr('train_ne_cdhit.txt')
feature


def ctc(input):
	a = input.rstrip('txt')
	output=a+'ctc.csv'
	df_out=ctc_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=ctc('train_po_cdhit.txt')
feature

feature=ctc('train_ne_cdhit.txt')
feature


def ctd(input):
	a = input.rstrip('txt')
	output=a+'ctd.csv'
	df_out=ctd_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=ctd('train_po_cdhit.txt')
feature

feature=ctd('train_ne_cdhit.txt')
feature


def paac(input):
	a = input.rstrip('txt')
	output=a+'paac.csv'
	df_out=paac_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=paac('train_po_cdhit.txt')
feature

feature=paac('train_ne_cdhit.txt')
feature


def apaac(input):
	a = input.rstrip('txt')
	output=a+'apaac.csv'
	df_out=apaac_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=apaac('train_po_cdhit.txt')
feature

feature=apaac('train_ne_cdhit.txt')
feature


def qos(input):
	a = input.rstrip('txt')
	output=a+'qos.csv'
	df_out=qos_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=qos('train_po_cdhit.txt')
feature

feature=qos('train_ne_cdhit.txt')
feature


def soc(input):
	a = input.rstrip('txt')
	output=a+'soc.csv'
	df_out=soc_wp(input, output)
	df_in=pd.read_csv(output)
	return df_in

feature=soc('train_po_cdhit.txt')
feature

feature=soc('train_ne_cdhit.txt')
feature

