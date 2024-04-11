# init .vsc.*
if (interactive() && Sys.getenv("RSTUDIO") == "") {
  source(file.path(Sys.getenv(if (.Platform$OS.type == "windows") "USERPROFILE" else "HOME"), ".vscode-R", "init.R"))
}

# use httpggd to view
if (interactive() && Sys.getenv("TERM_PROGRAM") == "vscode") {
  if ("httpgd" %in% .packages(all.available = TRUE)) {
    options(vsc.plot = FALSE)
    options(device = function(...) {
      httpgd::hgd(silent = TRUE)
      .vsc.browser(httpgd::hgd_url(history = FALSE), viewer = "Beside")
    })
  }
}

# rstudio package manager
if (.Platform$OS.type != "windows") {
  options(repos = c(REPO_NAME = "https://packagemanager.rstudio.com/cran/latest"))
  options(BioC_mirror = "https://packagemanager.rstudio.com/bioconductor")
}
