#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import factura
from webapp2_extras import jinja2

class MainHandler(webapp2.RequestHandler):
    def post(self):
        cif = self.request.get("edCIF", "Desconocido")
        nombre = self.request.get("edNombre", "Desconocido")
        direccion = self.request.get("edDireccion", "Desconocida")
        provincia = self.request.get("edProvincia", "Desconocida")
        codigoPostal = self.request.get("edCodigoPostal", 0)
        pais = self.request.get("edPais", "Desconocido")
        personaContacto = self.request.get("edPersonaContacto", "Desconocida")
        email = self.request.get("edEmail", "Desconocido")
        telefono = self.request.get("edTelefono", "Desconocido")
        concepto = self.request.get("edConcepto", "Desconocido")
        precio = self.request.get("edPrecio", 0)
        unidades = self.request.get("edUnidades", 0)
        importeBruto = self.request.get("edImporteBruto", 0)
        iva = self.request.get("edIVA", 0)
        importeTotal = self.request.get("edImporteTotal", 0)

        if len(cif.strip()) == 0:
            cif = "Desconocido"
        if len(nombre.strip()) == 0:
            nombre = "Desconocido"
        if len(direccion.strip()) == 0:
            direccion = "Desconocido"
        if len(provincia.strip()) == 0:
            provincia = "Desconocido"
        if codigoPostal <= 0:
            codigoPostal = 0
        if len(pais.strip()) == 0:
            pais = "Desconocido"
        if len(personaContacto.strip()) == 0:
            personaContacto = "Desconocido"
        if len(email.strip()) == 0:
            email = "Desconocido"
        if telefono <= 0:
            telefono = 0
        if len(concepto.strip()) == 0:
            concepto = "Desconocido"
        if precio <= 0:
            precio = 0
        if unidades <= 0:
            unidades = 0
        if importeBruto <= 0:
            importeBruto = 0
        if iva <= 0:
            iva = 0
        if importeTotal <= 0:
            importeTotal = 0

        linea = factura.LineaDetalle(concepto, precio, unidades, importeBruto, iva, importeTotal)
        jinja = jinja2.get_jinja2(app=self.app)

        valores_plantilla = {
            "nombre": nombre,
            "cif": cif,
            "direccion": direccion,
            "provincia": provincia,
            "codigoPostal": codigoPostal,
            "pais": pais,
            "personaContacto": personaContacto,
            "email": email,
            "telefono": telefono,
            "linea": linea
        }

        self.response.write(jinja.render_template("answer.html", **valores_plantilla))

app = webapp2.WSGIApplication([
    ('/factura', MainHandler)
], debug=True)
