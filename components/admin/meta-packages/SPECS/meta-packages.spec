#----------------------------------------------------------------------------bh-
# This RPM .spec file is part of the OpenHPC project.
#
# It may have been modified from the default version supplied by the underlying
# release package (if available) in order to apply patches, perform customized
# build/install configurations, and supply additional files to support
# desired integration conventions.
#
#----------------------------------------------------------------------------eh-

%include %{_sourcedir}/OHPC_macros
%{!?PROJ_DELIM: %global PROJ_DELIM -ohpc}

Summary: Meta-packages to ease installation
Name:    meta-packages
Version: 1.3.1
Release: 1
License: Apache-2.0
Group:   %{PROJ_NAME}/meta-package
URL:     https://github.com/openhpc/ohpc
Source0: LICENSE


BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
DocDir:    %{OHPC_PUB}/doc/contrib

%description

This is an internal package that is used to create groups as part
of the installation source setup.  Installation of this package does
not make sense.

%package -n %{PROJ_NAME}-autotools
Summary:   OpenHPC autotools
Requires:  autoconf%{PROJ_DELIM}
Requires:  automake%{PROJ_DELIM}
Requires:  libtool%{PROJ_DELIM}
%description -n %{PROJ_NAME}-autotools
Collection of GNU autotools packages

%package -n %{PROJ_NAME}-base
Summary:   OpenHPC base
Requires:  bc
Requires:  conman%{PROJ_DELIM}
Requires:  emacs-nox
Requires:  examples%{PROJ_DELIM}
Requires:  gdb
Requires:  ipmitool
Requires:  libstdc++-devel
Requires:  lmod%{PROJ_DELIM}
Requires:  losf%{PROJ_DELIM}
Requires:  make
Requires:  man
Requires:  net-tools
Requires:  nfs-utils
Requires:  ntp
Requires:  OpenIPMI
Requires:  pdsh%{PROJ_DELIM}
Requires:  screen
Requires:  sudo
%if 0%{?centos_version} || 0%{?rhel_version}
Requires:  binutils
Requires:  binutils-devel
Requires:  man-db
Requires:  yum-utils
%endif
%if 0%{?sles_version}
Requires:  glibc-locale
Requires:  libmlx4-rdmav2
Requires:  nfs-kernel-server
%endif
%description -n %{PROJ_NAME}-base
Collection of base packages

%package -n %{PROJ_NAME}-base-compute
Summary:   OpenHPC compute node base
Requires:  libicu
Requires:  libunwind
Requires:  numactl
%if 0%{?centos_version} || 0%{?rhel_version}
Requires:  cairo-devel
Requires:  libpciaccess
%endif
%if 0%{?sles_version}
Requires:  libcairo2
Requires:  libpciaccess0
%endif
%description -n %{PROJ_NAME}-base-compute
Collection of compute node base packages

%package -n %{PROJ_NAME}-ganglia
Summary:   OpenHPC Ganglia monitoring
Requires:  ganglia%{PROJ_DELIM}
Requires:  ganglia-devel%{PROJ_DELIM}
Requires:  ganglia-gmetad%{PROJ_DELIM}
Requires:  ganglia-gmond%{PROJ_DELIM}
Requires:  ganglia-gmond-python%{PROJ_DELIM}
Requires:  ganglia-web%{PROJ_DELIM}
%description -n %{PROJ_NAME}-ganglia
Collection of Ganglia monitoring and metrics packages

%package -n %{PROJ_NAME}-gnu7-io-libs
Summary:   OpenHPC IO libraries for GNU
Requires:  adios-gnu7-mpich%{PROJ_DELIM}
Requires:  adios-gnu7-openmpi%{PROJ_DELIM}
Requires:  hdf5-gnu7%{PROJ_DELIM}
Requires:  netcdf-cxx-gnu7-mpich%{PROJ_DELIM}
Requires:  netcdf-cxx-gnu7-openmpi%{PROJ_DELIM}
Requires:  netcdf-fortran-gnu7-mpich%{PROJ_DELIM}
Requires:  netcdf-fortran-gnu7-openmpi%{PROJ_DELIM}
Requires:  netcdf-gnu7-mpich%{PROJ_DELIM}
Requires:  netcdf-gnu7-openmpi%{PROJ_DELIM}
Requires:  phdf5-gnu7-mpich%{PROJ_DELIM}
Requires:  phdf5-gnu7-openmpi%{PROJ_DELIM}
%ifnarch aarch64
Requires:  adios-gnu7-mvapich2%{PROJ_DELIM}
Requires:  netcdf-cxx-gnu7-mvapich2%{PROJ_DELIM}
Requires:  netcdf-fortran-gnu7-mvapich2%{PROJ_DELIM}
Requires:  netcdf-gnu7-mvapich2%{PROJ_DELIM}
Requires:  phdf5-gnu7-mvapich2%{PROJ_DELIM}
%endif
%description -n %{PROJ_NAME}-gnu7-io-libs
Collection of IO library builds for use with GNU compiler toolchain

%package -n %{PROJ_NAME}-nagios
Summary:   OpenHPC Nagios monitoring
Requires:  nagios%{PROJ_DELIM}
Requires:  nagios-plugins-all%{PROJ_DELIM}
Requires:  nrpe%{PROJ_DELIM}
%description -n %{PROJ_NAME}-nagios
Collection of Nagios monitoring and metrics packages

%package -n %{PROJ_NAME}-gnu7-parallel-libs
Summary:   OpenHPC parallel libraries for GNU
Requires:  boost-gnu7-mpich%{PROJ_DELIM}
Requires:  boost-gnu7-openmpi%{PROJ_DELIM}
Requires:  fftw-gnu7-mpich%{PROJ_DELIM}
Requires:  fftw-gnu7-openmpi%{PROJ_DELIM}
Requires:  hypre-gnu7-mpich%{PROJ_DELIM}
Requires:  hypre-gnu7-openmpi%{PROJ_DELIM}
Requires:  mumps-gnu7-mpich%{PROJ_DELIM}
Requires:  mumps-gnu7-openmpi%{PROJ_DELIM}
Requires:  petsc-gnu7-mpich%{PROJ_DELIM}
Requires:  petsc-gnu7-openmpi%{PROJ_DELIM}
Requires:  scalapack-gnu7-mpich%{PROJ_DELIM}
Requires:  scalapack-gnu7-openmpi%{PROJ_DELIM}
Requires:  superlu_dist-gnu7-mpich%{PROJ_DELIM}
Requires:  superlu_dist-gnu7-openmpi%{PROJ_DELIM}
Requires:  trilinos-gnu7-mpich%{PROJ_DELIM}
Requires:  trilinos-gnu7-openmpi%{PROJ_DELIM}
%ifnarch aarch64
Requires:  boost-gnu7-mvapich2%{PROJ_DELIM}
Requires:  fftw-gnu7-mvapich2%{PROJ_DELIM}
Requires:  hypre-gnu7-mvapich2%{PROJ_DELIM}
Requires:  mumps-gnu7-mvapich2%{PROJ_DELIM}
Requires:  petsc-gnu7-mvapich2%{PROJ_DELIM}
Requires:  scalapack-gnu7-mvapich2%{PROJ_DELIM}
Requires:  superlu_dist-gnu7-mvapich2%{PROJ_DELIM}
Requires:  trilinos-gnu7-mvapich2%{PROJ_DELIM}
%endif
%description -n %{PROJ_NAME}-gnu7-parallel-libs
Collection of parallel library builds for use with GNU compiler toolchain

%package -n %{PROJ_NAME}-gnu7-mpich-parallel-libs
Summary:   OpenHPC parallel libraries for GNU and MPICH
Requires:  boost-gnu7-mpich%{PROJ_DELIM}
Requires:  fftw-gnu7-mpich%{PROJ_DELIM}
Requires:  hypre-gnu7-mpich%{PROJ_DELIM}
Requires:  mumps-gnu7-mpich%{PROJ_DELIM}
Requires:  petsc-gnu7-mpich%{PROJ_DELIM}
Requires:  scalapack-gnu7-mpich%{PROJ_DELIM}
Requires:  superlu_dist-gnu7-mpich%{PROJ_DELIM}
Requires:  trilinos-gnu7-mpich%{PROJ_DELIM}
%description -n %{PROJ_NAME}-gnu7-mpich-parallel-libs
Collection of parallel library builds for use with GNU compiler toolchain and the MPICH runtime

%package -n %{PROJ_NAME}-gnu7-openmpi-parallel-libs
Summary:   OpenHPC parallel libraries for GNU and OpenMPI
Requires:  boost-gnu7-openmpi%{PROJ_DELIM}
Requires:  fftw-gnu7-openmpi%{PROJ_DELIM}
Requires:  hypre-gnu7-openmpi%{PROJ_DELIM}
Requires:  mumps-gnu7-openmpi%{PROJ_DELIM}
Requires:  petsc-gnu7-openmpi%{PROJ_DELIM}
Requires:  scalapack-gnu7-openmpi%{PROJ_DELIM}
Requires:  superlu_dist-gnu7-openmpi%{PROJ_DELIM}
Requires:  trilinos-gnu7-openmpi%{PROJ_DELIM}
%description -n %{PROJ_NAME}-gnu7-openmpi-parallel-libs
Collection of parallel library builds for use with GNU compiler toolchain and the OpenMPI runtime

%package -n %{PROJ_NAME}-gnu7-perf-tools
Summary:   OpenHPC performance tools for GNU
Requires:  imb-gnu7-mpich%{PROJ_DELIM}
Requires:  imb-gnu7-openmpi%{PROJ_DELIM}
Requires:  mpiP-gnu7-mpich%{PROJ_DELIM}
Requires:  mpiP-gnu7-openmpi%{PROJ_DELIM}
Requires:  papi%{PROJ_DELIM}
Requires:  tau-gnu7-mpich%{PROJ_DELIM}
Requires:  tau-gnu7-openmpi%{PROJ_DELIM}
Requires:  scalasca-gnu7-mpich%{PROJ_DELIM}
Requires:  scalasca-gnu7-openmpi%{PROJ_DELIM}
%ifnarch aarch64
Requires:  imb-gnu7-mvapich2%{PROJ_DELIM}
Requires:  mpiP-gnu7-mvapich2%{PROJ_DELIM}
Requires:  tau-gnu7-mvapich2%{PROJ_DELIM}
Requires:  scalasca-gnu7-mvapich2%{PROJ_DELIM}
%endif
%description -n %{PROJ_NAME}-gnu7-perf-tools
Collection of performance tool builds for use with GNU compiler toolchain

%package -n %{PROJ_NAME}-gnu7-python-libs
Summary:   OpenHPC python libraries for GNU
Requires:  python-numpy-gnu7%{PROJ_DELIM}
Requires:  python-scipy-gnu7-mpich%{PROJ_DELIM}
Requires:  python-scipy-gnu7-openmpi%{PROJ_DELIM}
%ifnarch aarch64
Requires:  python-scipy-gnu7-mvapich2%{PROJ_DELIM}
%endif
%description -n %{PROJ_NAME}-gnu7-python-libs
Collection of python related library builds for use with GNU compiler toolchain

%package -n %{PROJ_NAME}-gnu7-runtimes
Summary:   OpenHPC runtimes for GNU
Requires:  ocr-gnu7%{PROJ_DELIM}
Requires:  singularity%{PROJ_DELIM}
%description -n %{PROJ_NAME}-gnu7-runtimes
Collection of runtimes for use with GNU compiler toolchain

%package -n %{PROJ_NAME}-gnu7-serial-libs
Summary:   OpenHPC serial libraries for GNU
Requires:  gsl-gnu7%{PROJ_DELIM}
Requires:  metis-gnu7%{PROJ_DELIM}
Requires:  openblas-gnu7%{PROJ_DELIM}
Requires:  R-gnu7%{PROJ_DELIM}
Requires:  superlu-gnu7%{PROJ_DELIM}
%description -n %{PROJ_NAME}-gnu7-serial-libs
Collection of serial library builds for use with GNU compiler toolchain

%package -n %{PROJ_NAME}-slurm-client
Summary:   OpenHPC client packages for SLURM
Requires:  slurm%{PROJ_DELIM}
Requires:  slurm-munge%{PROJ_DELIM}
Requires:  slurm-plugins%{PROJ_DELIM}
Requires:  slurm-sjobexit%{PROJ_DELIM}
Requires:  slurm-pam_slurm%{PROJ_DELIM}
Requires:  munge%{PROJ_DELIM}
%description -n %{PROJ_NAME}-slurm-client
Collection of client packages for SLURM

%package -n %{PROJ_NAME}-slurm-server
Summary:   OpenHPC server packages for SLURM
Requires:  slurm%{PROJ_DELIM}
Requires:  slurm-munge%{PROJ_DELIM}
Requires:  slurm-plugins%{PROJ_DELIM}
Requires:  slurm-perlapi%{PROJ_DELIM}
Requires:  slurm-devel%{PROJ_DELIM}
Requires:  slurm-slurmdbd%{PROJ_DELIM}
Requires:  slurm-sql%{PROJ_DELIM}
Requires:  slurm-slurmdb-direct%{PROJ_DELIM}
Requires:  munge%{PROJ_DELIM}
Requires:  munge-libs%{PROJ_DELIM}
Requires:  munge-devel%{PROJ_DELIM}
Requires:  pdsh-mod-slurm%{PROJ_DELIM}
%description -n %{PROJ_NAME}-slurm-server
Collection of server packages for SLURM

%package -n %{PROJ_NAME}-warewulf
Summary:   OpenHPC base packages for Warewulf
Requires:  warewulf-cluster%{PROJ_DELIM}
Requires:  warewulf-common%{PROJ_DELIM}
Requires:  warewulf-provision%{PROJ_DELIM}
Requires:  warewulf-provision-server%{PROJ_DELIM}
Requires:  warewulf-vnfs%{PROJ_DELIM}
%description -n %{PROJ_NAME}-warewulf
Collection of base packages for Warewulf provisioning

# x86_64 specific groups
%ifnarch aarch64
%package -n %{PROJ_NAME}-intel-io-libs
Summary:   OpenHPC IO libraries for Intel(R) Parallel Studio XE
Requires:  adios-gnu7-impi%{PROJ_DELIM}
Requires:  adios-intel-impi%{PROJ_DELIM}
Requires:  adios-intel-mpich%{PROJ_DELIM}
Requires:  adios-intel-mvapich2%{PROJ_DELIM}
Requires:  adios-intel-openmpi%{PROJ_DELIM}
Requires:  hdf5-intel%{PROJ_DELIM}
Requires:  netcdf-cxx-gnu7-impi%{PROJ_DELIM}
Requires:  netcdf-cxx-intel-impi%{PROJ_DELIM}
Requires:  netcdf-cxx-intel-mpich%{PROJ_DELIM}
Requires:  netcdf-cxx-intel-mvapich2%{PROJ_DELIM}
Requires:  netcdf-cxx-intel-openmpi%{PROJ_DELIM}
Requires:  netcdf-fortran-gnu7-impi%{PROJ_DELIM}
Requires:  netcdf-fortran-intel-impi%{PROJ_DELIM}
Requires:  netcdf-fortran-intel-mpich%{PROJ_DELIM}
Requires:  netcdf-fortran-intel-mvapich2%{PROJ_DELIM}
Requires:  netcdf-fortran-intel-openmpi%{PROJ_DELIM}
Requires:  netcdf-gnu7-impi%{PROJ_DELIM}
Requires:  netcdf-intel-impi%{PROJ_DELIM}
Requires:  netcdf-intel-mpich%{PROJ_DELIM}
Requires:  netcdf-intel-mvapich2%{PROJ_DELIM}
Requires:  netcdf-intel-openmpi%{PROJ_DELIM}
Requires:  phdf5-gnu7-impi%{PROJ_DELIM}
Requires:  phdf5-intel-impi%{PROJ_DELIM}
Requires:  phdf5-intel-mpich%{PROJ_DELIM}
Requires:  phdf5-intel-mvapich2%{PROJ_DELIM}
Requires:  phdf5-intel-openmpi%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-io-libs
Collection of IO library builds for use with Intel(R) Parallel Studio XE software suite

%package -n %{PROJ_NAME}-gnu7-mvapich2-parallel-libs
Summary:   OpenHPC parallel libraries for GNU and MVAPICH2
Requires:  boost-gnu7-mvapich2%{PROJ_DELIM}
Requires:  fftw-gnu7-mvapich2%{PROJ_DELIM}
Requires:  hypre-gnu7-mvapich2%{PROJ_DELIM}
Requires:  mumps-gnu7-mvapich2%{PROJ_DELIM}
Requires:  petsc-gnu7-mvapich2%{PROJ_DELIM}
Requires:  scalapack-gnu7-mvapich2%{PROJ_DELIM}
Requires:  superlu_dist-gnu7-mvapich2%{PROJ_DELIM}
Requires:  trilinos-gnu7-mvapich2%{PROJ_DELIM}
%description -n %{PROJ_NAME}-gnu7-mvapich2-parallel-libs
Collection of parallel library builds for use with GNU compiler toolchain and the MVAPICH2 runtime

%package -n %{PROJ_NAME}-intel-impi-parallel-libs
Summary:   OpenHPC parallel libraries for Intel(R) Parallel Studio XE and Intel(R) MPI Library
Requires:  boost-gnu7-impi%{PROJ_DELIM}
Requires:  boost-intel-impi%{PROJ_DELIM}
Requires:  hypre-gnu7-impi%{PROJ_DELIM}
Requires:  hypre-intel-impi%{PROJ_DELIM}
Requires:  mumps-gnu7-impi%{PROJ_DELIM}
Requires:  mumps-intel-impi%{PROJ_DELIM}
Requires:  petsc-gnu7-impi%{PROJ_DELIM}
Requires:  petsc-intel-impi%{PROJ_DELIM}
Requires:  scalapack-gnu7-impi%{PROJ_DELIM}
Requires:  scalapack-intel-impi%{PROJ_DELIM}
Requires:  superlu_dist-gnu7-impi%{PROJ_DELIM}
Requires:  superlu_dist-intel-impi%{PROJ_DELIM}
Requires:  trilinos-gnu7-impi%{PROJ_DELIM}
Requires:  trilinos-intel-impi%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-impi-parallel-libs
Collection of parallel library builds for use with Intel(R) Parallel Studio XE toolchain and the Intel(R) MPI Library

%package -n %{PROJ_NAME}-intel-mpich-parallel-libs
Summary:   OpenHPC parallel libraries for Intel(R) Parallel Studio XE and MPICH
Requires:  boost-intel-mpich%{PROJ_DELIM}
Requires:  hypre-intel-mpich%{PROJ_DELIM}
Requires:  mumps-intel-mpich%{PROJ_DELIM}
Requires:  petsc-intel-mpich%{PROJ_DELIM}
Requires:  scalapack-intel-mpich%{PROJ_DELIM}
Requires:  superlu_dist-intel-mpich%{PROJ_DELIM}
Requires:  trilinos-intel-mpich%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-mpich-parallel-libs
Collection of parallel library builds for use with Intel(R) Parallel Studio XE toolchain and the MPICH runtime

%package -n %{PROJ_NAME}-intel-mvapich2-parallel-libs
Summary:   OpenHPC parallel libraries for Intel(R) Parallel Studio XE and MVAPICH2
Requires:  boost-intel-mvapich2%{PROJ_DELIM}
Requires:  hypre-intel-mvapich2%{PROJ_DELIM}
Requires:  mumps-intel-mvapich2%{PROJ_DELIM}
Requires:  petsc-intel-mvapich2%{PROJ_DELIM}
Requires:  scalapack-intel-mvapich2%{PROJ_DELIM}
Requires:  superlu_dist-intel-mvapich2%{PROJ_DELIM}
Requires:  trilinos-intel-mvapich2%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-mvapich2-parallel-libs
Collection of parallel library builds for use with Intel(R) Parallel Studio XE toolchain and the MVAPICH2 runtime

%package -n %{PROJ_NAME}-intel-openmpi-parallel-libs
Summary:   OpenHPC parallel libraries for Intel(R) Parallel Studio XE and OpenMPI
Requires:  boost-intel-openmpi%{PROJ_DELIM}
Requires:  hypre-intel-openmpi%{PROJ_DELIM}
Requires:  mumps-intel-openmpi%{PROJ_DELIM}
Requires:  petsc-intel-openmpi%{PROJ_DELIM}
Requires:  scalapack-intel-openmpi%{PROJ_DELIM}
Requires:  superlu_dist-intel-openmpi%{PROJ_DELIM}
Requires:  trilinos-intel-openmpi%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-openmpi-parallel-libs
Collection of parallel library builds for use with Intel(R) Parallel Studio XE toolchain and the OpenMPI runtime

%package -n %{PROJ_NAME}-intel-perf-tools
Summary:   OpenHPC performance tools for Intel(R) Parallel Studio XE
Requires:  imb-gnu7-impi%{PROJ_DELIM}
Requires:  imb-intel-impi%{PROJ_DELIM}
Requires:  imb-intel-mpich%{PROJ_DELIM}
Requires:  imb-intel-mvapich2%{PROJ_DELIM}
Requires:  imb-intel-openmpi%{PROJ_DELIM}
Requires:  mpiP-gnu7-impi%{PROJ_DELIM}
Requires:  mpiP-intel-impi%{PROJ_DELIM}
Requires:  mpiP-intel-mpich%{PROJ_DELIM}
Requires:  mpiP-intel-mvapich2%{PROJ_DELIM}
Requires:  mpiP-intel-openmpi%{PROJ_DELIM}
Requires:  papi%{PROJ_DELIM}
Requires:  tau-gnu7-impi%{PROJ_DELIM}
Requires:  tau-intel-impi%{PROJ_DELIM}
Requires:  tau-intel-mpich%{PROJ_DELIM}
Requires:  tau-intel-mvapich2%{PROJ_DELIM}
Requires:  tau-intel-openmpi%{PROJ_DELIM}
Requires:  scalasca-gnu7-impi%{PROJ_DELIM}
Requires:  scalasca-intel-impi%{PROJ_DELIM}
Requires:  scalasca-intel-mpich%{PROJ_DELIM}
Requires:  scalasca-intel-mvapich2%{PROJ_DELIM}
Requires:  scalasca-intel-openmpi%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-perf-tools
Collection of performance tool builds for use with Intel(R) Parallel Studio XE toolchain

%package -n %{PROJ_NAME}-intel-python-libs
Summary:   OpenHPC python libraries for Intel(R) Parallel Studio XE
Requires:  python-numpy-intel%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-python-libs
Collection of python related library builds for use with Intel(R) Parallel Studio XE toolchain

%package -n %{PROJ_NAME}-intel-runtimes
Summary:   OpenHPC runtimes for Intel(R) Parallel Studio XE toolchain
Requires:  ocr-intel%{PROJ_DELIM}
Requires:  singularity%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-runtimes
Collection of runtimes for use with Intel(R) Parallel Studio XE toolchain

%package -n %{PROJ_NAME}-intel-serial-libs
Summary:   OpenHPC serial libraries for Intel(R) Parallel Studio XE
Requires:  metis-intel%{PROJ_DELIM}
Requires:  superlu-intel%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-serial-libs
Collection of serial library builds for use with Intel(R) Parallel Studio XE toolchain

%endif


%prep
%{__cp} %SOURCE0 .

%build

%install

%{__mkdir_p} ${RPM_BUILD_ROOT}/%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files

%files -n %{PROJ_NAME}-autotools
%files -n %{PROJ_NAME}-base
%files -n %{PROJ_NAME}-base-compute
%files -n %{PROJ_NAME}-ganglia
%files -n %{PROJ_NAME}-gnu7-io-libs
%files -n %{PROJ_NAME}-gnu7-parallel-libs
%files -n %{PROJ_NAME}-gnu7-mpich-parallel-libs
%files -n %{PROJ_NAME}-gnu7-openmpi-parallel-libs
%files -n %{PROJ_NAME}-gnu7-perf-tools
%files -n %{PROJ_NAME}-gnu7-python-libs
%files -n %{PROJ_NAME}-gnu7-runtimes
%files -n %{PROJ_NAME}-gnu7-serial-libs
%files -n %{PROJ_NAME}-nagios
%files -n %{PROJ_NAME}-slurm-client
%files -n %{PROJ_NAME}-slurm-server
%files -n %{PROJ_NAME}-warewulf
# x86_64 specific groups
%ifnarch aarch64
%files -n %{PROJ_NAME}-gnu7-mvapich2-parallel-libs
%files -n %{PROJ_NAME}-intel-io-libs
%files -n %{PROJ_NAME}-intel-impi-parallel-libs
%files -n %{PROJ_NAME}-intel-mpich-parallel-libs
%files -n %{PROJ_NAME}-intel-mvapich2-parallel-libs
%files -n %{PROJ_NAME}-intel-openmpi-parallel-libs
%files -n %{PROJ_NAME}-intel-perf-tools
%files -n %{PROJ_NAME}-intel-python-libs
%files -n %{PROJ_NAME}-intel-runtimes
%files -n %{PROJ_NAME}-intel-serial-libs
%endif

%changelog

