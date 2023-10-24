## Prepare inputs for the data-driven diphoton BDT training

1) Prepare the minimum photon ID distribution from background events.

From the `FGGLevel/` directory:
<pre><code>
python makeBkg040.py
python makeBkg4080.py
python makeBkg80inf.py
</code></pre>

This step generates the root files containing the minimum photon ID distribution for each considered background (diphoton events in [0,40]-[40,80]-[80,inf] GeV, gJets events in [0,40]-[40,80]-[80,inf] GeV, and QCD in [0,40]-[40,80]-[80,inf] GeV) and saves them in:
<pre><code>
DataDriven/bkg_histos/
</code></pre>

2) Generate the fake pdf distribution from the above mentioned processes.

Move in the `FGGLevel/DataDriven/` directory.

First of all, we need to produce a minimum photon ID distribution taking into account the above mentioned gJets and QCD samples except for the QCD [0,40] GeV one:
<pre><code>
python plotMinID.py
</code></pre>

The distributions are saved in the following file, used as input to compute the fake PDF and produce the sideband tree:
<pre><code>
minid_gjetqcd40.root ;
</code></pre>

Check the result of the spline (with some smooting) obtained from this file: this spline represents our fake PDF for the next steps of the data driven BDT.
<pre><code>
python spline_minID_fit.py
</code></pre>


<pre><code>
reweight_with_spline.py
</code></pre>
