'use strict';

define([
  'underscore',
  'backbone',
  'JST',
  'collections/agencies',
  'views/modals/agency'
  ], function (_, Backbone, JST, AgenciesCollection, AgencyModal) {
    var View;

    View = Backbone.View.extend({
      tagName: 'div',

      events: {
        'click button.add-btn': 'add',
        'click button.btn-create': 'onAdd',
        'click button.btn-edit': 'onEdit',
        'click button.btn-rm': 'onRemove',
        'click input[type="checkbox"]': 'onEditCheckbox'
      },

      template: JST.agencies,

      initialize: function(){
        this.collection = new AgenciesCollection();
        this.collection.on('add change remove reset', this.render, this);
        this.render();
        this.collection.fetch();
      },

      render: function () {
        this.$el.html(this.template({
          models: this.collection.toJSON()
        }));
        $('.main-view').empty().append(this.el);
        this.delegateEvents(this.events);
      },

      onRemove: function (e) {
        var $target = $(e.currentTarget),
          index = $target.closest('tr').data('index'),
          model = this.collection.at(index);

        e.preventDefault();
        model.destroy();
      },

      onAdd: function (e) {
        e.preventDefault();
        var model = new this.collection.model();
        var modal = new AgencyModal({
          model: model,
          el: $('#routeDataEditor')
        });
        modal.$el.modal('show');
      },

      onEdit: function (e) {
        var $target = $(e.currentTarget),
          index = $target.closest('tr').data('index'),
          model = this.collection.at(index),
          modal = new AgencyModal({
            model: model,
            el: $('#routeDataEditor')
        });
        modal.$el.modal('show');
      }
    });

    return View;
  });