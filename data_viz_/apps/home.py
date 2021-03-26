#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from app import app, server
import datetime
from skimage.transform import resize
import pickle
from transform import RGB2GrayTransformer, HogTransformer

import numpy as np
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("This is an animal classifier API", className="text-center")
                    , className="mb-4 mt-4")
        ]),
        dbc.Row([
            dbc.Col(html.Img(src="/assets/dog_cat_rabbit.jpg", height="300px")
                    , className="mb-4 text-center")
            ]),
        # dbc.Row([
        #     dbc.Col(html.H4(children='Animal Image Classfier'
        #                              ))
        #     ]),
        dbc.Row([
            dbc.Col(html.H5(children='This API predict which animal is on the image: dog, cat or rabbit:')                        
                    , className="mb-4")
            ]),
        dbc.Row([
            dbc.Col(html.H5(children='Please insert an animal image:')                        
                    , className="mb-4")
            ]),
        #dbc.Row([
        #    dbc.Col(dbc.Card(children=[html.H5(children='Chicken',
        #                                       className="text-center"),
        #                               html.Img(src="/assets/chicken.jpg", height="70px")]),),
        #    dbc.Col(dbc.Card(children=[html.H5(children='Monkey',
        #                                       className="text-center"),
        #                               html.Img(src="/assets/monkey.jpg", height="70px")]),),
            # dbc.Col(dbc.Card(children=[html.H5(children='Bear',
            #                                    className="text-center"),
            #                            html.Img(src="/assets/bear.jpg", height="70px")]),),
            #             dbc.Col(dbc.Card(children=[html.H5(children='Pandas',
            #                                    className="text-center"),
            #                            html.Img(src="/assets/panda.jpg", height="70px")]),),
            # dbc.Col(dbc.Card(children=[html.H5(children='Deer',
            #                                    className="text-center"),
            #                            html.Img(src="/assets/deer.jpg", height="70px")]),),
            # dbc.Col(dbc.Card(children=[html.H5(children='Eagle',
            #                                    className="text-center"),
            #                            html.Img(src="/assets/eagle.jpg", height="70px")]),),
            # dbc.Col(dbc.Card(children=[html.H5(children='Elephant',
            #                                    className="text-center"),
            #                            html.Img(src="/assets/elephant.jpg", height="70px")]),),
            # dbc.Col(dbc.Card(children=[html.H5(children='Spider',
            #                                    className="text-center"),
            #                            html.Img(src="/assets/spider.jpg", height="70px")]),className="mb-4"),
            # ]),
        dcc.Upload(
        id='upload-image',
        children=html.Div([
            'insert image '#,html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'color' : 'black',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'solid',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
            'background-color':'gray'
        },
        # Allow multiple files to be uploaded
        multiple=False
        ),
        # html.Div(id='output-image-upload', className="mb-4"),
        # dbc.Row([
        #     dbc.Col(html.H5(children='Animal Image Searcher')
        #             , className="mb-4"),]),
        # dbc.Row([
        #     dbc.Col(html.Img(src="/assets/pates.jpg", height="150px")
        #             , className="mb-4 text-center"),
        #     dbc.Col(dbc.Card(children=[html.H3(children='Google Image like Exclusive for Animals',
        #                                        className="text-center"),
        #                                dbc.Button("Go on Animal Engine", href="/page1",
        #                                                            color="primary",
        #                                                 className="mt-3"),                              
        #                                ],
        #                      body=True, color="dark", outline=True,className="align-self-center")
        #             , width=8, className="mb-4 text-center"),
        #     dbc.Col(html.Img(src="/assets/pates.jpg", height="150px")
        #             , className="mb-4 text-center")
        # ]),
        # html.A("Get the full code of app on my github repositary",
        #        href="https://github.com/Ludo-R/")
])])