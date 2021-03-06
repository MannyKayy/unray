"use strict";

import expect = require('expect.js');

import * as ndarray from 'ndarray';

import * as dw from "../src/datawidgets";
import * as pw from "../src/plotwidgets";

import { createTestModel } from './utils.spec';

import * as factory from "./modelfactory.spec";


describe('plotwidgets', function() {

    describe('SurfacePlotModel', function() {
        it('should fail to construct if not given a mesh', function() {
            expect(createTestModel).withArgs(pw.SurfacePlotModel, {}).to.throwException();
        });
        it('should be constructable with only a mesh', function() {
            const mesh = factory.createMesh();
            const attribs = { mesh };
            const plot = createTestModel(pw.SurfacePlotModel, attribs);
            expect(plot.get('_model_name')).to.be("SurfacePlotModel");
        });
        it('should be constructable with wireframe params', function() {
            const mesh = factory.createMesh();

            const wireframe = factory.createWireframeParams();
            wireframe.set('enable', true);

            const attribs = { mesh, wireframe };
            const plot = createTestModel(pw.SurfacePlotModel, attribs);
            expect(plot.get('_model_name')).to.be("SurfacePlotModel");

            expect(plot.get('wireframe').get('enable')).to.be(true);
        });
        it('should be constructable with constant color', function() {
            const mesh = factory.createMesh();
            const color = factory.createColorConstant();

            const attribs = { mesh, color };
            const plot = createTestModel(pw.SurfacePlotModel, attribs);
            expect(plot.get('_model_name')).to.be("SurfacePlotModel");
        });
        it('should be constructable with color field', function() {
            const mesh = factory.createMesh();
            const color = factory.createColorField();

            const attribs = { mesh, color };
            const plot = createTestModel(pw.SurfacePlotModel, attribs);
            expect(plot.get('_model_name')).to.be("SurfacePlotModel");
        });
    });

    describe('IsosurfacePlotModel', function() {
        it('should fail to construct if not given a mesh', function() {
            expect(createTestModel).withArgs(pw.IsosurfacePlotModel, {}).to.throwException();
        });
        it('should be constructable with only a mesh', function() {
            const mesh = factory.createMesh();
            const attribs = { mesh };
            const plot = createTestModel(pw.IsosurfacePlotModel, attribs);
            expect(plot.get('_model_name')).to.be("IsosurfacePlotModel");
        });
    });

    describe('XrayPlotModel', function() {
        it('should fail to construct if not given a mesh', function() {
            expect(createTestModel).withArgs(pw.XrayPlotModel, {}).to.throwException();
        });
        it('should be constructable with only a mesh', function() {
            const mesh = factory.createMesh();
            const attribs = { mesh };
            const plot = createTestModel(pw.XrayPlotModel, attribs);
            expect(plot.get('_model_name')).to.be("XrayPlotModel");
        });
        it('should be constructable with a constant density', function() {
            const mesh = factory.createMesh();
            const density = factory.createScalarConstant();

            const attribs = { mesh, density };
            const plot = createTestModel(pw.XrayPlotModel, attribs);
            expect(plot.get('_model_name')).to.be("XrayPlotModel");
        });
        it('should be constructable with a density field', function() {
            const mesh = factory.createMesh();
            const density = factory.createScalarField();

            const attribs = { mesh, density };
            const plot = createTestModel(pw.XrayPlotModel, attribs);
            expect(plot.get('_model_name')).to.be("XrayPlotModel");
        });
    });

    describe('SumPlotModel', function() {
        it('should fail to construct if not given a mesh', function() {
            expect(createTestModel).withArgs(pw.SumPlotModel, {}).to.throwException();
        });
        it('should be constructable with only a mesh', function() {
            const mesh = factory.createMesh();
            const attribs = { mesh };
            const plot = createTestModel(pw.SumPlotModel, attribs);
            expect(plot.get('_model_name')).to.be("SumPlotModel");
        });
    });

    describe('MinPlotModel', function() {
        it('should fail to construct if not given a mesh', function() {
            expect(createTestModel).withArgs(pw.MinPlotModel, {}).to.throwException();
        });
        it('should be constructable with only a mesh', function() {
            const mesh = factory.createMesh();
            const attribs = { mesh };
            const plot = createTestModel(pw.MinPlotModel, attribs);
            expect(plot.get('_model_name')).to.be("MinPlotModel");
        });
    });

    describe('MaxPlotModel', function() {
        it('should fail to construct if not given a mesh', function() {
            expect(createTestModel).withArgs(pw.MaxPlotModel, {}).to.throwException();
        });
        it('should be constructable with only a mesh', function() {
            const mesh = factory.createMesh();
            const attribs = { mesh };
            const plot = createTestModel(pw.MaxPlotModel, attribs);
            expect(plot.get('_model_name')).to.be("MaxPlotModel");
        });
    });

    describe('VolumePlotModel', function() {
        it('should fail to construct if not given a mesh', function() {
            expect(createTestModel).withArgs(pw.VolumePlotModel, {}).to.throwException();
        });
        it('should be constructable with only a mesh', function() {
            const mesh = factory.createMesh();
            const attribs = { mesh };
            const plot = createTestModel(pw.VolumePlotModel, attribs);
            expect(plot.get('_model_name')).to.be("VolumePlotModel");
        });
    });

});
