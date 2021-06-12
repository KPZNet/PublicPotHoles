from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

from forms import ContactForm, ContactFormXY, AEPotHoleForm, AEWorkOrderForm
from PotHoleModels import DataStore, PotHole, WorkOrder

app = Flask ( __name__ )
app.debug = True
app.config['SECRET_KEY'] = 'a really really really really long secret key'

ds = DataStore()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='PHTRS Home',
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='CSU Global CS505',
        year=datetime.now().year,
        developer='Kenneth Ceglia'
    )


@app.route('/AEPotHole/', methods=['get', 'post'])
def AEPotHole():
    form = AEPotHoleForm()
    if form.validate_on_submit():
        f = form
        ph = PotHole()
        ph.district = f.district.data
        ph.streetAddress = f.streetAddress.data
        ph.size = f.size.data
        ph.location = f.location.data
        ph.priority = 5

        ds.AddPotHole(ph)
        # db logic goes here
        return redirect(url_for('AEPotHole'))

    return render_template('AEPotHole.html', form=form)

@app.route('/AEWorkOrder/', methods=['get', 'post'])
def AEWorkOrder():
    form = AEWorkOrderForm()
    if form.validate_on_submit():
        f = form
        wo = WorkOrder()
        wo.potHoleID = f.potHoleID.data
        wo.hoursApplied = f.hoursApplied.data
        wo.repairCrewID = f.repairCrewID.data
        wo.equipmentAssigned = f.equipmentAssigned.data
        wo.fillerMaterial = f.fillerMaterial.data
        wo.holeStatus = f.holeStatus.data
        wo.numberOfWorkers = f.numberOfWorkers.data

        ds.AddWorkOrder(wo)

        return redirect(url_for('AEWorkOrder'))

    return render_template('AEWorkOrder.html', form=form)

# A decorator used to tell the application
# which URL is associated function
@app.route('/AllPotHolesReport')
def AllPotHolesReport():
    potholeReport = ds.GetAllPotHolesReport()
    for f in potholeReport:
        print( str(f) )
    return render_template('AllPotHolesReport.html', phReport = potholeReport)

# A decorator used to tell the application
# which URL is associated function
@app.route('/AllWorkOrdersReport')
def AllWorkOrdersReport():
    workOrderReport = ds.GetAllWorkOrdersReport()
    for f in workOrderReport:
        print( str(f) )
    return render_template('AllWorkOrdersReport.html', woReport = workOrderReport)


if __name__ == '__main__' :
    app.run ()
