*> \brief \b SCHKQ3
*
*  =========== DOCUMENTATION ===========
*
* Online html documentation available at 
*            http://www.netlib.org/lapack/explore-html/ 
*
*  Definition:
*  ===========
*
*       SUBROUTINE SCHKQ3( DOTYPE, NM, MVAL, NN, NVAL, NNB, NBVAL, NXVAL,
*                          THRESH, A, COPYA, S, TAU, WORK, IWORK,
*                          NOUT )
* 
*       .. Scalar Arguments ..
*       INTEGER            NM, NN, NNB, NOUT
*       REAL               THRESH
*       ..
*       .. Array Arguments ..
*       LOGICAL            DOTYPE( * )
*       INTEGER            IWORK( * ), MVAL( * ), NBVAL( * ), NVAL( * ),
*      $                   NXVAL( * )
*       REAL               A( * ), COPYA( * ), S( * ),
*      $                   TAU( * ), WORK( * )
*       ..
*  
*
*> \par Purpose:
*  =============
*>
*> \verbatim
*>
*> SCHKQ3 tests SGEQP3.
*> \endverbatim
*
*  Arguments:
*  ==========
*
*> \param[in] DOTYPE
*> \verbatim
*>          DOTYPE is LOGICAL array, dimension (NTYPES)
*>          The matrix types to be used for testing.  Matrices of type j
*>          (for 1 <= j <= NTYPES) are used for testing if DOTYPE(j) =
*>          .TRUE.; if DOTYPE(j) = .FALSE., then type j is not used.
*> \endverbatim
*>
*> \param[in] NM
*> \verbatim
*>          NM is INTEGER
*>          The number of values of M contained in the vector MVAL.
*> \endverbatim
*>
*> \param[in] MVAL
*> \verbatim
*>          MVAL is INTEGER array, dimension (NM)
*>          The values of the matrix row dimension M.
*> \endverbatim
*>
*> \param[in] NN
*> \verbatim
*>          NN is INTEGER
*>          The number of values of N contained in the vector NVAL.
*> \endverbatim
*>
*> \param[in] NVAL
*> \verbatim
*>          NVAL is INTEGER array, dimension (NN)
*>          The values of the matrix column dimension N.
*> \endverbatim
*>
*> \param[in] NNB
*> \verbatim
*>          NNB is INTEGER
*>          The number of values of NB and NX contained in the
*>          vectors NBVAL and NXVAL.  The blocking parameters are used
*>          in pairs (NB,NX).
*> \endverbatim
*>
*> \param[in] NBVAL
*> \verbatim
*>          NBVAL is INTEGER array, dimension (NNB)
*>          The values of the blocksize NB.
*> \endverbatim
*>
*> \param[in] NXVAL
*> \verbatim
*>          NXVAL is INTEGER array, dimension (NNB)
*>          The values of the crossover point NX.
*> \endverbatim
*>
*> \param[in] THRESH
*> \verbatim
*>          THRESH is REAL
*>          The threshold value for the test ratios.  A result is
*>          included in the output file if RESULT >= THRESH.  To have
*>          every test ratio printed, use THRESH = 0.
*> \endverbatim
*>
*> \param[out] A
*> \verbatim
*>          A is REAL array, dimension (MMAX*NMAX)
*>          where MMAX is the maximum value of M in MVAL and NMAX is the
*>          maximum value of N in NVAL.
*> \endverbatim
*>
*> \param[out] COPYA
*> \verbatim
*>          COPYA is REAL array, dimension (MMAX*NMAX)
*> \endverbatim
*>
*> \param[out] S
*> \verbatim
*>          S is REAL array, dimension
*>                      (min(MMAX,NMAX))
*> \endverbatim
*>
*> \param[out] TAU
*> \verbatim
*>          TAU is REAL array, dimension (MMAX)
*> \endverbatim
*>
*> \param[out] WORK
*> \verbatim
*>          WORK is REAL array, dimension
*>                      (MMAX*NMAX + 4*NMAX + MMAX)
*> \endverbatim
*>
*> \param[out] IWORK
*> \verbatim
*>          IWORK is INTEGER array, dimension (2*NMAX)
*> \endverbatim
*>
*> \param[in] NOUT
*> \verbatim
*>          NOUT is INTEGER
*>          The unit number for output.
*> \endverbatim
*
*  Authors:
*  ========
*
*> \author Univ. of Tennessee 
*> \author Univ. of California Berkeley 
*> \author Univ. of Colorado Denver 
*> \author NAG Ltd. 
*
*> \date November 2011
*
*> \ingroup single_lin
*
*  =====================================================================
      SUBROUTINE SCHKQ3( DOTYPE, NM, MVAL, NN, NVAL, NNB, NBVAL, NXVAL,
     $                   THRESH, A, COPYA, S, TAU, WORK, IWORK,
     $                   NOUT )

      IMPLICIT NONE
      INCLUDE 'plasmaf.h'
*
*  -- LAPACK test routine (version 3.4.0) --
*  -- LAPACK is a software package provided by Univ. of Tennessee,    --
*  -- Univ. of California Berkeley, Univ. of Colorado Denver and NAG Ltd..--
*     November 2011
*
*     .. Scalar Arguments ..
      INTEGER            NM, NN, NNB, NOUT
      REAL               THRESH
*     ..
*     .. Array Arguments ..
      LOGICAL            DOTYPE( * )
      INTEGER            IWORK( * ), MVAL( * ), NBVAL( * ), NVAL( * ),
     $                   NXVAL( * )
      REAL               A( * ), COPYA( * ), S( * ),
     $                   TAU( * ), WORK( * )
*     ..
*
*  =====================================================================
*
*     .. Parameters ..
      INTEGER            NTYPES
*                      was NTYPES = 6; types > 3 are not yet implemented in PLASMA
*                      also changed in schkaa.f and stest.in
      PARAMETER          ( NTYPES = 3 )
      INTEGER            NTESTS
      PARAMETER          ( NTESTS = 3 )
      REAL               ONE, ZERO
      PARAMETER          ( ONE = 1.0E0, ZERO = 0.0E0 )
*     ..
*     .. Local Scalars ..
      CHARACTER*3        PATH
      INTEGER            I, IHIGH, ILOW, IM, IMODE, IN, INB, INFO,
     $                   ISTEP, K, LDA, LWORK, M, MNMIN, MODE, N,
     $                   NB, NERRS, NFAIL, NRUN, NX
      REAL               EPS
*     ..
*     .. Local Arrays ..
      INTEGER            ISEED( 4 ), ISEEDY( 4 )
      REAL               RESULT( NTESTS )
*     ..
*     .. External Functions ..
      REAL               SLAMCH, SQPT01, SQRT11, SQRT12
      EXTERNAL           SLAMCH, SQPT01, SQRT11, SQRT12
*     ..
*     .. External Subroutines ..
      EXTERNAL           ALAHD, ALASUM, ICOPY, SLACPY, SLAORD,
     $                   PLASMA_SGEQP3, SLASET, SLATMS, XLAENV
*     ..
*     .. Intrinsic Functions ..
      INTRINSIC          MAX, MIN
*     ..
*     .. Scalars in Common ..
      LOGICAL            LERR, OK
      CHARACTER*32       SRNAMT
      INTEGER            INFOT, IOUNIT
*     ..
*     .. Common blocks ..
      COMMON             / INFOC / INFOT, IOUNIT, OK, LERR
      COMMON             / SRNAMC / SRNAMT
*     ..
*     .. Data statements ..
      DATA               ISEEDY / 1988, 1989, 1990, 1991 /
*     ..
*     .. Executable Statements ..
*
*     Initialize constants and the random number seed.
*
      PATH( 1: 1 ) = 'Single precision'
      PATH( 2: 3 ) = 'Q3'
      NRUN = 0
      NFAIL = 0
      NERRS = 0
      DO 10 I = 1, 4
         ISEED( I ) = ISEEDY( I )
   10 CONTINUE
      EPS = SLAMCH( 'Epsilon' )
      INFOT = 0
*
      DO 90 IM = 1, NM
*
*        Do for each value of M in MVAL.
*
         M = MVAL( IM )
         LDA = MAX( 1, M )
*
         DO 80 IN = 1, NN
*
*           Do for each value of N in NVAL.
*
            N = NVAL( IN )
            MNMIN = MIN( M, N )
            LWORK = MAX( 1, M*MAX( M, N )+4*MNMIN+MAX( M, N ),
     $                   M*N + 2*MNMIN + 4*N )
*
            DO 70 IMODE = 1, NTYPES
               IF( .NOT.DOTYPE( IMODE ) )
     $            GO TO 70
*
*              Do for each type of matrix
*                 1:  zero matrix
*                 2:  one small singular value
*                 3:  geometric distribution of singular values
*                 4:  n-1 small singular values, first n/2 columns fixed   [disabled in PLASMA]
*                 5:  n-1 small singular values, last n/2 columns fixed    [disabled in PLASMA]
*                 6:  n-1 small singular values, every second column fixed [disabled in PLASMA]
*
               MODE = IMODE
               IF( IMODE.GT.3 )
     $            MODE = 1
*
*              Generate test matrix of size m by n using
*              singular value distribution indicated by `mode'.
*
               DO 20 I = 1, N
                  IWORK( I ) = 0
   20          CONTINUE
               IF( IMODE.EQ.1 ) THEN
                  CALL SLASET( 'Full', M, N, ZERO, ZERO, COPYA, LDA )
                  DO 30 I = 1, MNMIN
                     S( I ) = ZERO
   30             CONTINUE
               ELSE
                  CALL SLATMS( M, N, 'Uniform', ISEED, 'Nonsymm', S,
     $                         MODE, ONE / EPS, ONE, M, N, 'No packing',
     $                         COPYA, LDA, WORK, INFO )
                  IF( IMODE.GE.4 ) THEN
                     IF( IMODE.EQ.4 ) THEN
                        ILOW = 1
                        ISTEP = 1
                        IHIGH = MAX( 1, N / 2 )
                     ELSE IF( IMODE.EQ.5 ) THEN
                        ILOW = MAX( 1, N / 2 )
                        ISTEP = 1
                        IHIGH = N
                     ELSE IF( IMODE.EQ.6 ) THEN
                        ILOW = 1
                        ISTEP = 2
                        IHIGH = N
                     END IF
                     DO 40 I = ILOW, IHIGH, ISTEP
                        IWORK( I ) = 1
   40                CONTINUE
                  END IF
                  CALL SLAORD( 'Decreasing', MNMIN, S, 1 )
               END IF
*
               DO 60 INB = 1, NNB
*
*                 Do for each pair of values (NB,NX) in NBVAL and NXVAL.
*
                  NB = NBVAL( INB )
                  CALL XLAENV( 1, NB )
                  NX = NXVAL( INB )
                  CALL XLAENV( 3, NX )
                  CALL PLASMA_SET( PLASMA_TILE_SIZE, NB, INFO )
*
*                 Get a working copy of COPYA into A and a copy of
*                 vector IWORK.
*
                  CALL SLACPY( 'All', M, N, COPYA, LDA, A, LDA )
                  CALL ICOPY( N, IWORK( 1 ), 1, IWORK( N+1 ), 1 )
*
*                 Compute the QP3 factorization of A
*
*                  print '(a,i3,a,i3,a,i3,a,i3,a,i3)',
*     $                  'sgeqp3 m=', m, '  n=', n, '  lda=', lda,
*     $                  '  nb=', nb, '  imode=', imode
*
                  SRNAMT = 'SGEQP3'
                  CALL PLASMA_SGEQP3( M, N, A, LDA, IWORK( N+1 ),
     $                                TAU, WORK,
     $                                WORK((N+1)*NB), INFO )     
*
*                 Compute norm(svd(a) - svd(r))
*
                  RESULT( 1 ) = SQRT12( M, N, A, LDA, S, WORK,
     $                          LWORK )
*
*                 Compute norm( A*P - Q*R )
*
                  RESULT( 2 ) = SQPT01( M, N, MNMIN, COPYA, A, LDA, TAU,
     $                          IWORK( N+1 ), WORK, LWORK )
*
*                 Compute Q'*Q
*
                  RESULT( 3 ) = SQRT11( M, MNMIN, A, LDA, TAU, WORK,
     $                          LWORK )
*
*                 Print information about the tests that did not pass
*                 the threshold.
*
                  DO 50 K = 1, NTESTS
                     IF( RESULT( K ).GE.THRESH ) THEN
                        IF( NFAIL.EQ.0 .AND. NERRS.EQ.0 )
     $                     CALL ALAHD( NOUT, PATH )
                        WRITE( NOUT, FMT = 9999 )'SGEQP3', M, N, NB,
     $                     IMODE, K, RESULT( K )
                        NFAIL = NFAIL + 1
                     END IF
   50             CONTINUE
                  NRUN = NRUN + NTESTS
*
   60          CONTINUE
   70       CONTINUE
   80    CONTINUE
   90 CONTINUE
*
*     Print a summary of the results.
*
      CALL ALASUM( PATH, NOUT, NFAIL, NRUN, NERRS )
*
 9999 FORMAT( 1X, A, ' M =', I5, ', N =', I5, ', NB =', I4, ', type ',
     $      I2, ', test ', I2, ', ratio =', G12.5 )
*
*     End of SCHKQ3
*
      END