#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify, request, g, abort, url_for, current_app
from .. import db
from ..models import Route
from ..models import Trip
from . import api
from flask.ext.login import login_required

@api.route('/routes/')
def get_routes():
    routes = Route.query.order_by(Route.route_short_name).all()
    return jsonify({
        'routes': [item.to_json for item in routes]
    })


@api.route('/routes/<id>')
def get_route(id):
    item = Route.query.get_or_404(id)
    return jsonify(item.to_json)


@api.route('/routes/', methods=['POST'])
def add_route():
    item = Route(**request.json)
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_json), 201, \
        {'Location': url_for('api.get_route', id=item.route_id, _external=True)}

@login_required
@api.route('/routes/<id>', methods=['PUT'])
def edit_route(id):
    data = request.json
    item = Route.query.get_or_404(data.get('route_id'))
    item = Route(**data)
    db.session.merge(item)
    return jsonify(item.to_json)


@api.route('/routes/<id>', methods=['DELETE'])
def delete_route(id):
    route = Route.query.filter_by(route_id = id).one()
    db.session.delete(route)
    db.session.commit()
    return jsonify({'status': 'success'}), 200


@api.route('/route/<route_id>/trips')
def get_route_trips(route_id):
    trips = Trip.query.filter(Trip.route_id == route_id)\
        .order_by(Trip.trip_headsign).all()
    return jsonify({'trips': [trip.to_json for trip in trips]}), 200
