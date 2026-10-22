# Project images and editorial selection

The project collection contains sixteen independent Chinese/English introductions.
Each explains purpose, architecture, operating stages, results, analysis and scope.
Only source images that remain useful and readable at page size are included.

## Selected images

| Project | Image | Interpretation |
| --- | --- | --- |
| ECsnap | Owner-provided instrument photograph | Prototype enclosure, display and electrode interface; no concentration-performance claim |
| Dual-Axis Gravity Controller | Archived running-vector-mean plot | Model simulation with a 0.380 G reference, not physical gravity reduction |
| Biological Image Analysis | Plant contours and area labels | Saved segmentation output; values depend on original scale and parameters |
| Medical Image Analysis | Two archived digit-classification curves | Training/validation accuracy and loss; historical results |
| Data Structures | Source-0 shortest-path tree | Archived graph result; original graph remains linked at the source repository |
| AFPGA | Lab 8 board photograph | Archived LED and seven-segment state, interpreted with HPS source |

The source photos and plots are copied without modifying their visual contents.
`content/media-sources.json` records source labels and SHA-256 hashes. Local full
paths and complete research documents are kept outside the published repository.

## Not selected

The review excluded cluttered bench views, tiny terminal captures, repeated
frames, slide backgrounds, logos, other people's portraits, generic illustrations
and generated apparatus renders. A weighted-graph raster with overlapping edge
labels was also excluded; its clearer shortest-path tree was retained.

The sweat-pressure screenshot contained unrelated phone status information and
added little result evidence at page scale, so it was not selected. Other research
projects currently use clear architecture and process explanations, with a note
that no suitable result photo has been selected. Images are not added just to
populate a gallery, and explanatory diagrams are not described as experimental
results.

## Sources and verification

Public README files were checked through the GitHub connector. Source snapshots:

- ThermoPatch `6c0871d`; archived v1.0.1 release/test material.
- SpaceCellCam `f78a64a`; capture sequence and configuration.
- Space BMC `5117feb`; published 15-check Questa simulation record.
- nRF54L15/MLX90614 `6a502ab`; hardware, BLE and power-analysis documents.
- Galaxy Watch `6a75d5f`; tracker lifecycle and SDK requirements.
- Taipei Bus `6d9db5e`; data, route model, UI and tests.
- Medical imaging `f80beaf`; historical metrics and reviewed aggregate plots.
- Data structures `9e9d2f7`; archived graph images and verification records.
- AFPGA curated public checkout; Lab 8 source and archived result image.

The unchanged Taipei Bus snapshot's Node test suite was executed in this review:
61 tests passed, zero failed. This is software evidence, not a measurement of road
position or arrival accuracy. No device flashing, acquisition experiment, model
training or new clinical evaluation was performed.

The three owner-provided research images were inspected individually against
their documents and captions. No patient images or personal profiles were selected.

## Maintenance

`content/case_studies.json` is the editable source for all sixteen pages, their
language pairs, source links and galleries. Run `python tools/build_case_studies.py`
after changing content. It also adds a detail-page link to every homepage card.
Use `python tools/build_share_images.py` after changing project names or tags.

Before adding a photo, inspect it at full size and in the actual responsive page.
Give it a precise caption, identify whether it is a prototype, archived result,
analysis output or simulation, and confirm that it provides information worth
the reading space it occupies.
