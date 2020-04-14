class Factura:
    def __init__(self, fecha, lineas):
        self._fecha = fecha
        self._lineas = lineas

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def lineas(self):
        return self._lineas

    @lineas.setter
    def lineas(self, lineas):
        self._lineas = lineas


class LineaDetalle:
    def __init__(self, concepto, precio, unidades, importe_bruto, iva, importe_total):
        self._concepto = concepto
        self._precio = precio
        self._unidades = unidades
        self._importeBruto = importe_bruto
        self._iva = iva
        self._importeTotal = importe_total

    @property
    def concepto(self):
        return self._concepto

    @concepto.setter
    def concepto(self, concepto):
        self._concepto = concepto

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @property
    def unidades(self):
        return self._unidades

    @unidades.setter
    def unidades(self, unidades):
        self._unidades = unidades

    @property
    def importeBruto(self):
        return self._importeBruto

    @importeBruto.setter
    def importeBruto(self, importe_bruto):
        self._importeBruto = importe_bruto

    @property
    def iva(self):
        return self._iva

    @iva.setter
    def iva(self, iva):
        self._iva = iva

    @property
    def importeTotal(self):
        return self._importeTotal

    @importeTotal.setter
    def importeTotal(self, importe_total):
        self._importeTotal = importe_total

    def __str__(self):

        toRet = " \t Concepto: " + self._concepto + "\n"
        toRet += "\t Precio por unidad: " + self._precio + "\n"
        toRet += "\t Unidades: " + self._unidades + "\n"
        toRet += "\t Importe Bruto: " + self._importeBruto + "\n"
        toRet += "\t % IVA: " + self._iva + "\n"
        toRet += "\t Importe Total: " + self._importeTotal + "\n"

        return toRet