#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Float
from base import Base, Entity

class Shape(Base, Entity):
  __tablename__ = 'shapes'
  shape_id = Column(String(50), primary_key=True)
  shape_pt_lat = Column(Float(precision=53))
  shape_pt_lon = Column(Float(precision=53))
  shape_pt_time = Column(String(50))
  shape_pt_sequence = Column(Integer, primary_key=True)